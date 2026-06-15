from datetime import datetime

from pydantic import BaseModel


class TrainingHistoryItem(
    BaseModel
):
    session_id: str

    created_at: datetime

    completed_at: datetime | None

    correct_answers: int

    total_questions: int

    accuracy: int