"""Create trains table.

Revision ID: d58957ea71ed
Revises: 7c6b586b5f55
Create Date: 2024-10-02 14:30:03.921070

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d58957ea71ed"
down_revision: Union[str, None] = "7c6b586b5f55"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "trains",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("station_id", sa.Integer(), nullable=False),
        sa.Column("train_type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["station_id"], ["stations.id"], onupdate="CASCADE", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["train_type_id"],
            ["train_types.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("trains")
    # ### end Alembic commands ###
