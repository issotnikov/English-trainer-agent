from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.db.base_class import Base
from app.models.user import User
from app.models.word import Word