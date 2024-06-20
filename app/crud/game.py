from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models, schema


def get_game(db: Session, game_id: int) -> schema.Game | None:
    return db.query(models.Game).where(models.Game.id == game_id).first()


def create_game(db: Session, game: schema.GameCreate) -> schema.Game:
    db_game = models.Game(
        player_1=game.player_1,
        player_2=game.player_2,
        is_player_2_cpu=game.is_player_2_cpu,
    )
    db.add(db_game)
    return db_game


def update_game_results(db: Session, game_id: int) -> None:
    query = (
        db.query(models.Round.outcome, func.count(models.Round.id))
        .where(models.Round.game_id == game_id)
        .group_by(models.Round.outcome)
        .all()
    )
    if not query:
        return

    results = dict(query)
    db.query(models.Game).where(models.Game.id == game_id).update(
        {
            "player_1_wins": results.get(models.OutcomeEnum.PLAYER_1, 0),
            "player_2_wins": results.get(models.OutcomeEnum.PLAYER_2, 0),
            "draws": results.get(models.OutcomeEnum.PLAYER_2, 0),
        }
    )
