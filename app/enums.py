from enum import Enum


class GameStatus(str, Enum):
    backlog = "backlog"
    playing = "playing"
    completed = "completed"
    dropped = "dropped"