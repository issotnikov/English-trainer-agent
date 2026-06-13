"""add_category_id_to_training_sessions

Revision ID: 73f0b23261ad
Revises: 81f27afdb6df
Create Date: 2026-06-12 23:05:53.840263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "73f0b23261ad"
down_revision: Union[str, Sequence[str], None] = "81f27afdb6df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "training_sessions",
        sa.Column(
            "category_id",
            sa.String(),
            nullable=True
        )
    )

    op.create_foreign_key(
        "fk_training_sessions_category_id",
        "training_sessions",
        "categories",
        ["category_id"],
        ["id"]
    )


def downgrade() -> None:

    op.drop_constraint(
        "fk_training_sessions_category_id",
        "training_sessions",
        type_="foreignkey"
    )

    op.drop_column(
        "training_sessions",
        "category_id"
    )