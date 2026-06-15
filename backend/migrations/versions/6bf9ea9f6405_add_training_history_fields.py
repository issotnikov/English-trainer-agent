"""add_training_history_fields

Revision ID: 6bf9ea9f6405
Revises: 5aaea853d3fd
Create Date: 2026-06-14 08:43:42.378616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bf9ea9f6405'
down_revision: Union[str, Sequence[str], None] = '5aaea853d3fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "training_sessions",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        )
    )

    op.add_column(
        "training_sessions",
        sa.Column(
            "completed_at",
            sa.DateTime(),
            nullable=True
        )
    )

    op.add_column(
        "training_sessions",
        sa.Column(
            "is_completed",
            sa.Boolean(),
            nullable=False,
            server_default="false"
        )
    )


def downgrade() -> None:

    op.drop_column(
        "training_sessions",
        "is_completed"
    )

    op.drop_column(
        "training_sessions",
        "completed_at"
    )

    op.drop_column(
        "training_sessions",
        "created_at"
    )