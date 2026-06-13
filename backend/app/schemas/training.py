from uuid import UUID

from pydantic import BaseModel


class TrainingAnswerRequest(BaseModel):
    answer: str


class NextWordResponse(BaseModel):
    word_id: UUID
    english: str


class TrainingAnswerResponse(BaseModel):
    is_correct: bool
    correct_answer: str

    next_word: NextWordResponse | None = None

    finished: bool = False

    correct_answers: int | None = None
    total_questions: int | None = None
    accuracy: int | None = None