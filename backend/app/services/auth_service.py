from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(
        self,
        email: str,
        password: str
    ):

        existing_user = self.repo.get_by_email(email)

        if existing_user:
            raise ValueError(
                "User already exists"
            )

        user = User(
            email=email,
            hashed_password=hash_password(password)
        )

        return self.repo.create(user)

    def login(
        self,
        email: str,
        password: str
    ):

        user = self.repo.get_by_email(email)

        if not user:
            raise ValueError(
                "Invalid credentials"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise ValueError(
                "Invalid credentials"
            )

        return create_access_token(
            subject=user.id
        )