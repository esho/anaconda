"""initial

Revision ID: 98a9c9c5fdf3
Revises: 
Create Date: 2024-06-20 02:43:35.027168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98a9c9c5fdf3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_1', sa.String(), nullable=False),
    sa.Column('player_2', sa.String(), nullable=True),
    sa.Column('is_player_2_cpu', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('player_1_wins', sa.String(), server_default='0', nullable=False),
    sa.Column('player_2_wins', sa.String(), server_default='0', nullable=False),
    sa.Column('draws', sa.Integer(), server_default='0', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('round',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('player_1_play', sa.Enum('ROCK', 'PAPER', 'SCISSOR', name='playenum'), nullable=False),
    sa.Column('player_2_play', sa.Enum('ROCK', 'PAPER', 'SCISSOR', name='playenum'), nullable=False),
    sa.Column('outcome', sa.Enum('PLAYER_1', 'PLAYER_2', 'DRAW', name='outcomeenum'), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('round')
    op.drop_table('game')
    # ### end Alembic commands ###