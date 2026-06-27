from pydantic import BaseModel


class ImportWordItem(BaseModel):
    english: str
    russian: str
    category_id: str


class ImportWordsResponse(BaseModel):
    imported: int
    skipped: int