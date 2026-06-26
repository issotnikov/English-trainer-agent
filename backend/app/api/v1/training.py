from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db

from app.models.user import User

from app.repositories.word_repository import (
    WordRepository
)

from app.repositories.training_session_repository import (
    TrainingSessionRepository
)

from app.schemas.training_session import (
    TrainingStartResponse
)

from app.schemas.training import (
    TrainingAnswerRequest,
    TrainingAnswerResponse
)

from app.schemas.training_history import (
    TrainingHistoryItem
)

from app.schemas.training_stats import (
    TrainingStatsResponse
)

from app.services.training_service import (
    TrainingService
)

from app.schemas.training_start import (
    TrainingStartRequest
)

from app.schemas.word_progress import (
    WordProgressResponse
)

from app.schemas.hard_word import (
    HardWordResponse
)

router = APIRouter(
    prefix="/training",
    tags=["training"]
)


@router.post(
    "/start",
    response_model=TrainingStartResponse
)
def start_training(
    request: TrainingStartRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = TrainingSessionRepository(
        db
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    result = service.start_training(
        user_id=current_user.id,
        category_id=request.category_id
    )

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="No words found"
        )

    return result


@router.post(
    "/{session_id}/answer",
    response_model=TrainingAnswerResponse,
    response_model_exclude_none=True
)
def answer_training(
    session_id: str,
    request: TrainingAnswerRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = TrainingSessionRepository(
        db
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    result = service.answer_training(
        session_id=session_id,
        user_id=current_user.id,
        answer=request.answer
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Training session not found"
        )

    return result

@router.get(
    "/history",
    response_model=list[TrainingHistoryItem]
)
def get_training_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = TrainingSessionRepository(
        db
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    return service.get_history(
        current_user.id
    )

@router.get(
    "/stats",
    response_model=TrainingStatsResponse
)
def get_training_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = TrainingSessionRepository(
        db
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    return service.get_stats(
        current_user.id
    )

@router.get(
    "/words/progress",
    response_model=list[
        WordProgressResponse
    ]
)
def get_word_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = TrainingSessionRepository(
        db
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    return service.get_word_progress(
        current_user.id
    )

@router.get(
    "/hard-words",
    response_model=list[
        HardWordResponse
    ]
)
def get_hard_words(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    word_repo = WordRepository(db)

    session_repo = (
        TrainingSessionRepository(db)
    )

    service = TrainingService(
        word_repo=word_repo,
        session_repo=session_repo
    )

    return service.get_hard_words(
        current_user.id
    )