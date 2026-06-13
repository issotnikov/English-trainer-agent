from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db

from app.models.user import User

from app.schemas.category import (
    CategoryCreate,
    CategoryResponse
)

from app.schemas.word import (
    WordResponse
)

from app.repositories.category_repository import (
    CategoryRepository
)

from app.repositories.word_repository import (
    WordRepository
)

from app.services.category_service import (
    CategoryService
)

from app.services.word_service import (
    WordService
)

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@router.post(
    "",
    response_model=CategoryResponse
)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    repo = CategoryRepository(db)

    service = CategoryService(repo)

    return service.create_category(
        name=data.name,
        user_id=current_user.id
    )


@router.get(
    "",
    response_model=list[CategoryResponse]
)
def get_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    repo = CategoryRepository(db)

    service = CategoryService(repo)

    return service.get_user_categories(
        user_id=current_user.id
    )


@router.delete(
    "/{category_id}"
)
def delete_category(
    category_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    repo = CategoryRepository(db)

    service = CategoryService(repo)

    success = service.delete_category(
        category_id=category_id,
        user_id=current_user.id
    )

    return {
        "success": success
    }


@router.get(
    "/{category_id}/words",
    response_model=list[WordResponse]
)
def get_category_words(
    category_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    repo = WordRepository(db)

    service = WordService(repo)

    return service.get_category_words(
        category_id=category_id,
        user_id=current_user.id
    )