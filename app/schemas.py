from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

from app.enums import GameStatus


class GameCreate(SQLModel):
    title: str = Field(min_length=1, max_length=150)
    genre: str = Field(min_length=1, max_length=80)
    platform: str = Field(min_length=1, max_length=50)
    status: GameStatus
    score: Optional[int] = Field(default=None, ge=0, le=10)
    release_year: Optional[int] = Field(default=None, ge=1970, le=2100)


class GameUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=150)
    genre: Optional[str] = Field(default=None, min_length=1, max_length=80)
    platform: Optional[str] = Field(default=None, min_length=1, max_length=50)
    status: Optional[GameStatus] = None
    score: Optional[int] = Field(default=None, ge=0, le=10)
    release_year: Optional[int] = Field(default=None, ge=1970, le=2100)


class GameRead(SQLModel):
    id: int
    title: str
    genre: str
    platform: str
    status: GameStatus
    score: Optional[int] = None
    release_year: Optional[int] = None
    created_at: datetime
    updated_at: datetime