import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class PlayEnum(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class OutcomeEnum(enum.Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    DRAW = 3


class Round(Base):
    """A Game Round. Records each interaction between two players"""

    __tablename__ = "round"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
    player_1_play = Column(Enum(PlayEnum), nullable=False)
    player_2_play = Column(Enum(PlayEnum), nullable=False)
    outcome = Column(Enum(OutcomeEnum), nullable=False)
    created = Column(DateTime(timezone=True), server_default=func.now())

    game = relationship("Game", back_populates="rounds")
