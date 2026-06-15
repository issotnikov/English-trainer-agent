from datetime import datetime

from pydantic import BaseModel


class WordProgressResponse(
    BaseModel
):
    word_id: str

    english: str

    correct_answers: int

    wrong_answers: int

    accuracy: int

    last_trained_at: datetime | None