"""add_word_order_to_training_sessions

Revision ID: 5aaea853d3fd
Revises: 73f0b23261ad
Create Date: 2026-06-13 21:20:29.101213
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5aaea853d3fd"
down_revision: Union[str, Sequence[str], None] = "73f0b23261ad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "training_sessions",
        sa.Column(
            "word_order",
            sa.Text(),
            nullable=False,
            server_default="[]"
        )
    )


def downgrade() -> None:

    op.drop_column(
        "training_sessions",
        "word_order"
    )