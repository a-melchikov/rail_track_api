"""Updated the name train_station_association.

Revision ID: 4a662489f2ad
Revises: e8adec54cd87
Create Date: 2024-10-08 20:48:24.386037

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4a662489f2ad"
down_revision: Union[str, None] = "e8adec54cd87"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "train_station_association",
        sa.Column("train_id", sa.Integer(), nullable=False),
        sa.Column("station_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["station_id"], ["stations.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["train_id"], ["trains.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("train_id", "station_id"),
    )
    op.drop_table("train_station")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "train_station",
        sa.Column("train_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("station_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["station_id"],
            ["stations.id"],
            name="train_station_station_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["train_id"],
            ["trains.id"],
            name="train_station_train_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("train_id", "station_id", name="train_station_pkey"),
    )
    op.drop_table("train_station_association")
    # ### end Alembic commands ###
