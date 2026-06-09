from pydantic import BaseModel


class WordCreate(BaseModel):
    english: str
    russian: str
    category_id: str


class WordResponse(BaseModel):
    id: str
    english: str
    russian: str

    class Config:
        from_attributes = True
class WordResponse(BaseModel):
    id: str
    english: str
    russian: str
    category_id: str  # добавьте, если хотите вернуть category_id

    class Config:
        from_attributes = True