from datetime import datetime
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import Session, select

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
    session: Session = Depends(get_session)
):
    statement = select(Game)

    if status:
        statement = statement.where(Game.status == status)

    if platform:
        statement = statement.where(Game.platform == platform)

    games = session.exec(statement).all()
    return games


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