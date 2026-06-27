from sqlalchemy.orm import Session
from sqlalchemy import or_

from datetime import datetime
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

    def get_words_for_review(
        self,
        user_id: str,
        category_id: str | None = None
    ) -> list[Word]:

        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .filter(
                or_(
                    Word.next_review_at.is_(None),
                    Word.next_review_at <= datetime.utcnow()
                )
            )
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

    def update_training_result(
        self,
        word: Word,
        is_correct: bool
    ) -> Word:

        from datetime import datetime
        from datetime import timedelta

        review_intervals = {
            0: 1,
            1: 3,
            2: 7,
            3: 14,
            4: 30,
            5: 60,
            6: 90
        }

        if is_correct:

            word.correct_answers += 1

            word.difficulty = max(
                0.0,
                word.difficulty - 0.05
            )

            word.repetition_level = min(
                6,
                word.repetition_level + 1
            )

        else:

            word.wrong_answers += 1

            word.difficulty = min(
                1.0,
                word.difficulty + 0.10
            )

            word.repetition_level = max(
                0,
                word.repetition_level - 1
            )

        word.last_trained_at = datetime.utcnow()

        days = review_intervals[
            word.repetition_level
        ]

        word.next_review_at = (
            datetime.utcnow()
            + timedelta(days=days)
        )

        self.db.add(word)
        self.db.commit()
        self.db.refresh(word)

        return word

    def get_progress(
        self,
        user_id: str
    ):
        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .all()
        )

    def get_review_queue(
        self,
        user_id: str
    ) -> list[Word]:

        from datetime import datetime

        due_words = (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .filter(
                (Word.next_review_at == None)
                |
                (Word.next_review_at <= datetime.utcnow())
            )
            .order_by(
                Word.difficulty.desc(),
                Word.next_review_at.asc()
            )
            .all()
        )

        if due_words:
            return due_words

        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .order_by(
                Word.next_review_at.asc()
            )
            .all()
        )

    def get_hard_words(
        self,
        user_id: str
    ):

        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .filter(
                Word.difficulty >= 0.7
            )
            .order_by(
                Word.difficulty.desc()
            )
            .all()
        )

    def export_words(
        self,
        user_id: str
    ) -> list[Word]:

        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id
            )
            .order_by(
                Word.english
            )
            .all()
        )

    def exists(
        self,
        english: str,
        user_id: str
    ) -> bool:

        return (
            self.db.query(Word)
            .filter(
                Word.user_id == user_id,
                Word.english == english
            )
            .first()
            is not None
        )