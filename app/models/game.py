from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Game(Base):
    """Game model"""
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    player_1 = Column(String, nullable=False)
    player_2 = Column(String, nullable=True)
    is_player_2_cpu = Column(Boolean, nullable=True, server_default='f')
    player_1_wins = Column(String, nullable=False, server_default='0')
    player_2_wins = Column(String, nullable=False, server_default='0')
    draws = Column(Integer, nullable=False, server_default='0')
    created = Column(DateTime(timezone=True), server_default=func.now())

    rounds = relationship("Round", back_populates="game")
