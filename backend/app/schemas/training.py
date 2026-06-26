from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict


class TrainingAnswerRequest(BaseModel):
    answer: str


class NextWordResponse(BaseModel):
    word_id: UUID
    english: str


class TrainingAnswerResponse(BaseModel):

    model_config = ConfigDict(
        ser_json_exclude_none=True
    )
    
    is_correct: bool
    correct_answer: str

    next_word: NextWordResponse | None = None

    finished: bool = False

    correct_answers: int | None = None
    total_questions: int | None = None
    accuracy: int | None = None