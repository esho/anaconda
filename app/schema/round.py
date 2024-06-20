from datetime import datetime

from pydantic import BaseModel

from app.models import PlayEnum, OutcomeEnum


class RoundBase(BaseModel):
    player_1_play: PlayEnum
    player_2_play: PlayEnum


class RoundCreate(RoundBase):
    player_1_play: PlayEnum
    player_2_play: PlayEnum | None = None


class RoundModelBase(RoundBase):
    id: int
    game_id: int
    outcome: OutcomeEnum
    created: datetime


class RoundModel(RoundModelBase):
    pass


class Round(RoundModel):
    pass
