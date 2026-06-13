from sqlalchemy.orm import Session

from app.models.word import Word


class WordRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        english: str,
        russian: str,
        user_id: str,
        category_id: str
    ) -> Word:

        word = Word(
            english=english,
            russian=russian,
            user_id=user_id,
            category_id=category_id
        )

        self.db.add(word)
        self.db.commit()
        self.db.refresh(word)

        return word

    def get_by_user_id(
        self,
        user_id: str
    ) -> list[Word]:

        return (
            self.db.query(Word)
            .filter(Word.user_id == user_id)
            .all()
        )

    def get_by_category_id(
        self,
        category_id: str
    ) -> list[Word]:

        return (
            self.db.query(Word)
            .filter(Word.category_id == category_id)
            .all()
        )

    def get_by_category_and_user(
        self,
        category_id: str,
        user_id: str
    ) -> list[Word]:

        return (
            self.db.query(Word)
            .filter(
                Word.category_id == category_id,
                Word.user_id == user_id
            )
            .all()
        )

    def delete(
        self,
        word_id: str,
        user_id: str
    ) -> bool:

        word = (
            self.db.query(Word)
            .filter(
                Word.id == word_id,
                Word.user_id == user_id
            )
            .first()
        )

        if not word:
            return False

        self.db.delete(word)
        self.db.commit()

        return True