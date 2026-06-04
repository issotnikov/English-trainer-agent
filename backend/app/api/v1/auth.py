from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.auth import (
    TokenResponse,
    UserLogin,
    UserRegister,
)
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    payload: UserRegister,
    db: Session = Depends(get_db)
):

    service = AuthService(db)

    try:
        user = service.register(
            payload.email,
            payload.password
        )

        return {
            "id": user.id,
            "email": user.email
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    payload: UserLogin,
    db: Session = Depends(get_db)
):

    service = AuthService(db)

    try:
        token = service.login(
            payload.email,
            payload.password
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )