from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db

from app.models.user import User

from app.schemas.word import (
    WordCreate,
    WordResponse
)

from app.repositories.word_repository import (
    WordRepository
)

from app.services.word_service import WordService


router = APIRouter(
    prefix="/words",
    tags=["words"]
)


@router.post(
    "",
    response_model=WordResponse
)
def create_word(
    data: WordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    repo = WordRepository(db)

    service = WordService(repo)

    return service.create_word(
        english=data.english,
        russian=data.russian,
        user_id=current_user.id,
        category_id=data.category_id
    )


@router.get(
    "",
    response_model=list[WordResponse]
)
def get_words(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    repo = WordRepository(db)
    service = WordService(repo)

    return service.get_user_words(
        user_id=current_user.id
    )

@router.delete("/{word_id}")
def delete_word(
    word_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    repo = WordRepository(db)
    service = WordService(repo)

    success = service.delete_word(
        word_id=word_id,
        user_id=current_user.id
    )

    return {"success": success}