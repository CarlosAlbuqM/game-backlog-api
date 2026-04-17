from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import Session, select
from sqlalchemy import func

from app.database import get_session
from app.models import Game
from app.schemas import GameCreate, GameUpdate, GameRead

app = FastAPI(title="Game Backlog API")


@app.get("/")
def read_root():
    return {"message": "Game Backlog API is running!"}


@app.post("/games", response_model=GameRead, status_code=201)
def create_game(game_data: GameCreate, session: Session = Depends(get_session)):
    game = Game(**game_data.model_dump())
    session.add(game)
    session.commit()
    session.refresh(game)
    return game


@app.get("/games", response_model=list[GameRead])
def list_games(
    status: Optional[str] = Query(default=None),
    platform: Optional[str] = Query(default=None),
    genre: Optional[str] = Query(default=None),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: Session = Depends(get_session)
):
    statement = select(Game)

    if status:
        statement = statement.where(Game.status == status)

    if platform:
        statement = statement.where(Game.platform == platform)

    if genre:
        statement = statement.where(Game.genre == genre)

    statement = statement.offset(offset).limit(limit)

    games = session.exec(statement).all()
    return games

@app.get("/games/summary")
def get_games_summary(session: Session = Depends(get_session)):
    total_games = session.exec(
        select(func.count()).select_from(Game)
    ).one()

    completed = session.exec(
        select(func.count()).where(Game.status == "completed")
    ).one()

    playing = session.exec(
        select(func.count()).where(Game.status == "playing")
    ).one()

    backlog = session.exec(
        select(func.count()).where(Game.status == "backlog")
    ).one()

    dropped = session.exec(
        select(func.count()).where(Game.status == "dropped")
    ).one()

    return {
        "total_games": total_games,
        "completed": completed,
        "playing": playing,
        "backlog": backlog,
        "dropped": dropped
    }

@app.get("/games/summary/genres")
def get_games_by_genre(session: Session = Depends(get_session)):
    statement = (
        select(Game.genre, func.count().label("count"))
        .group_by(Game.genre)
        .order_by(func.count().desc())
    )

    results = session.exec(statement).all()

    return [
        {"genre": genre, "count": count}
        for genre, count in results
    ]


@app.get("/games/{game_id}", response_model=GameRead)
def get_game(game_id: int, session: Session = Depends(get_session)):
    game = session.get(Game, game_id)

    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    return game


@app.put("/games/{game_id}", response_model=GameRead)
def update_game(
    game_id: int,
    game_data: GameUpdate,
    session: Session = Depends(get_session)
):
    game = session.get(Game, game_id)

    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    update_data = game_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(game, key, value)

    game.updated_at = datetime.now()

    session.add(game)
    session.commit()
    session.refresh(game)

    return game


@app.delete("/games/{game_id}", status_code=204)
def delete_game(game_id: int, session: Session = Depends(get_session)):
    game = session.get(Game, game_id)

    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    session.delete(game)
    session.commit()
    return

