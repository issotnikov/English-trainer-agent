"""add_word_progress_fields

Revision ID: 5afd13a7fd38
Revises: 6bf9ea9f6405
Create Date: 2026-06-15

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5afd13a7fd38"

down_revision: Union[str, Sequence[str], None] = (
    "6bf9ea9f6405"
)

branch_labels = None

depends_on = None


def upgrade():

    op.add_column(
        "words",
        sa.Column(
            "correct_answers",
            sa.Integer(),
            nullable=False,
            server_default="0"
        )
    )

    op.add_column(
        "words",
        sa.Column(
            "wrong_answers",
            sa.Integer(),
            nullable=False,
            server_default="0"
        )
    )

    op.add_column(
        "words",
        sa.Column(
            "last_trained_at",
            sa.DateTime(),
            nullable=True
        )
    )


def downgrade():

    op.drop_column(
        "words",
        "last_trained_at"
    )

    op.drop_column(
        "words",
        "wrong_answers"
    )

    op.drop_column(
        "words",
        "correct_answers"
    )