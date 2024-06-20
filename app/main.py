from typing import Generator

from fastapi import Depends, FastAPI, HTTPException
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
    try:
        db_game = crud.create_game(db, game)
    except ValueError:
        pass
    db.commit()
    db.refresh(db_game)
    return db_game


@app.get("/game/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)) -> schema.Game:
    db_game = crud.get_game(db, game_id)
    if not db_game:
        raise HTTPException(status_code=404)
    return crud.get_game(db, game_id)


@app.post("/game/{game_id}/round")
def create_round(
    game_id: int, round: schema.RoundCreate, db: Session = Depends(get_db)
) -> schema.Round:
    try:
        db_round = crud.create_round(db, game_id, round)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    db.flush()
    crud.update_game_results(db, game_id)
    db.commit()
    db.refresh(db_round)
    return db_round


@app.get("/game/{game_id}/round/")
def list_rounds(game_id: int, db: Session = Depends(get_db)) -> list[schema.Round]:
    return crud.get_rounds(db, game_id)


@app.get("/game/{game_id}/round/{round_id}")
def get_round(
    game_id: int, round_id: int, db: Session = Depends(get_db)
) -> schema.Round:
    db_round = crud.get_round(db, game_id, round_id)
    if not db_round:
        raise HTTPException(status_code=404)
    return db_round
