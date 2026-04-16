from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from app.enums import GameStatus

class Game(SQLModel, table=True):
    __tablename__ = "games"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=150)
    genre: str = Field(max_length=80)
    platform: str = Field(max_length=50)
    status: GameStatus = Field(max_length=20)
    score: Optional[int] = Field(default=None, ge=0, le=10)
    release_year: Optional[int] = Field(default=None, ge=1970, le=2100)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)