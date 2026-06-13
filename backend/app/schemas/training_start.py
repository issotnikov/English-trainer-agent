from pydantic import BaseModel


class TrainingStartRequest(BaseModel):
    category_id: str | None = None