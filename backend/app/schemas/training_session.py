from pydantic import BaseModel


class TrainingStartRequest(
    BaseModel
):
    category_id: str | None = None


class TrainingStartResponse(
    BaseModel
):
    session_id: str
    word_id: str
    english: str