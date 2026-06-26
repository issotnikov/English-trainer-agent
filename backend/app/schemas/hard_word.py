from datetime import datetime

from pydantic import BaseModel


class HardWordResponse(
    BaseModel
):
    word_id: str
    english: str
    russian: str

    difficulty: float

    correct_answers: int
    wrong_answers: int

    repetition_level: int

    next_review_at: datetime | None