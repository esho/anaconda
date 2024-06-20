from typing import Generator

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, schema
from .database import SessionLocal


app = FastAPI()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/game")
def create_game(game: schema.GameCreate, db: Session = Depends(get_db)) -> schema.Game:
    return crud.create_game(db, game)


@app.get("/game/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)) -> schema.Game:
    return crud.get_game(db, game_id)


@app.post("/game/{game_id}/round")
def create_round(
    game_id: int, round: schema.RoundCreate, db: Session = Depends(get_db)
) -> schema.Round:
    return crud.create_round(db, game_id, round)


@app.get("/game/{game_id}/round/")
def list_rounds(game_id: int, db: Session = Depends(get_db)) -> list[schema.Round]:
    return crud.get_rounds(db, game_id)


@app.get("/game/{game_id}/round/{round_id}")
def get_round(
    game_id: int, round_id: int, db: Session = Depends(get_db)
) -> schema.Round:
    return crud.get_round(db, game_id, round_id)
