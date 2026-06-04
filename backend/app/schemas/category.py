from pydantic import BaseModel
from pydantic import ConfigDict


class CategoryCreate(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )