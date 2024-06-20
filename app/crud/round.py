import random

from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from app import models, schema
from app.crud.game import update_game_results


PLAY_OUTCOME_MAPPING = {
    models.PlayEnum.PAPER: models.PlayEnum.ROCK,
    models.PlayEnum.ROCK: models.PlayEnum.SCISSOR,
    models.PlayEnum.SCISSOR: models.PlayEnum.PAPER,
}


def _computer_cpu_play() -> models.PlayEnum:
    return random.choice(list(models.PlayEnum))


def _compute_outcome(
    player_1: models.PlayEnum, player_2: models.PlayEnum
) -> models.OutcomeEnum:
    if player_1 == player_2:
        return models.OutcomeEnum.DRAW
    if PLAY_OUTCOME_MAPPING[player_1] == player_2:
        return models.OutcomeEnum.PLAYER_1
    if PLAY_OUTCOME_MAPPING[player_2] == player_1:
        return models.OutcomeEnum.PLAYER_2
    raise ValueError("Incompatible play")


def get_round(db: Session, game_id: int, round_id: int) -> schema.Round | None:
    return (
        db.query(models.Round)
        .where(models.Round.id == round_id, models.Round.game_id == game_id)
        .first()
    )


def get_rounds(db: Session, game_id: int) -> list[schema.Round]:
    return db.query(models.Round).where(models.Round.game_id == game_id).all()


def create_round(db: Session, game_id: int, round: schema.RoundCreate) -> schema.Round:
    if db.query(
        exists().where(models.Game.is_player_2_cpu == True, models.Game.id == game_id)
    ).scalar():
        if round.player_2_play is not None:
            raise ValueError(
                "`player_2_play` must be `null` if `is_player_2_cpu` is `true`"
            )
        round.player_2_play = _computer_cpu_play()
    else:
        if round.player_2_play is None:
            raise ValueError(
                "`player_2_play` cannot be `null` if `is_player_2_cpu` is `false`"
            )

    outcome = _compute_outcome(round.player_1_play, round.player_2_play)
    db_round = models.Round(
        game_id=game_id,
        player_1_play=round.player_1_play,
        player_2_play=round.player_2_play,
        outcome=outcome,
    )
    db.add(db_round)

    return db_round
