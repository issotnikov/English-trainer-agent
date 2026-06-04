from pydantic import BaseModel


class WordCreate(BaseModel):
    english: str
    russian: str


class WordResponse(BaseModel):
    id: str
    english: str
    russian: str

    class Config:
        from_attributes = True