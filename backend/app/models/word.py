from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy import String
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
        ForeignKey("users.id")
    )