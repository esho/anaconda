from datetime import datetime

from pydantic import BaseModel, model_validator


class GameBase(BaseModel):
    player_1: str
    player_2: str | None = None
    is_player_2_cpu: bool


class GameCreate(GameBase):
    is_player_2_cpu: bool | None = False

    @model_validator(mode="after")
    def validate_is_player_2_cpu(self):
        if self.player_2 and self.is_player_2_cpu:
            raise ValueError(
                "Cannot set `is_player_2_cpu` to `true` and set `player_2` to non-null"
            )
        return self

    @model_validator(mode="after")
    def validate_distinct_player_names(self):
        if self.player_1 == self.player_2:
            raise ValueError("`player_1` and `player_2` cannot have same value")
        return self


class GameModelBase(GameBase):
    id: int
    player_1_wins: int
    player_2_wins: int
    draws: int
    created: datetime


class GameModel(GameModelBase):
    pass


class Game(GameModel):
    pass
