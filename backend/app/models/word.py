from uuid import uuid4

from sqlalchemy import Integer
from sqlalchemy import DateTime

from datetime import datetime

from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base_class import Base


class Word(Base):
    __tablename__ = "words"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    english: Mapped[str] = mapped_column(
        String(255)
    )

    russian: Mapped[str] = mapped_column(
        String(255)
    )

    user_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("users.id"),
        nullable=False
    )

    category_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("categories.id"),
        nullable=False
    )

    correct_answers: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    wrong_answers: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    last_trained_at: Mapped[datetime | None] = (
        mapped_column(
            DateTime,
            nullable=True
        )
    )