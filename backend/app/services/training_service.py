from app.repositories.word_repository import (
    WordRepository
)

from app.repositories.training_session_repository import (
    TrainingSessionRepository
)


class TrainingService:

    def __init__(
        self,
        word_repo: WordRepository,
        session_repo: TrainingSessionRepository
    ):
        self.word_repo = word_repo
        self.session_repo = session_repo

    def start_training(
        self,
        user_id: str,
        category_id: str | None = None
    ):

        if category_id:

            words = (
                self.word_repo
                .get_by_category_and_user(
                    category_id=category_id,
                    user_id=user_id
                )
            )

        else:

            words = self.word_repo.get_by_user_id(
                user_id=user_id
            )

        if not words:
            return None

        session = self.session_repo.create(
            user_id=user_id,
            category_id=category_id,
            total_questions=len(words)
        )

        first_word = words[0]

        return {
            "session_id": session.id,
            "word_id": first_word.id,
            "english": first_word.english
        }

    def answer_training(
        self,
        session_id: str,
        user_id: str,
        answer: str
    ):

        session = self.session_repo.get_by_id(
            session_id
        )

        if not session:
            return None

        if session.user_id != user_id:
            return None

        if session.category_id:

            words = (
                self.word_repo
                .get_by_category_and_user(
                    category_id=session.category_id,
                    user_id=user_id
                )
            )

        else:

            words = self.word_repo.get_by_user_id(
                user_id=user_id
            )

        if not words:
            return None

        if session.current_index >= len(words):
            return None

        current_word = words[
            session.current_index
        ]

        is_correct = (
            answer.strip().lower()
            ==
            current_word.russian.strip().lower()
        )

        if is_correct:
            session.correct_answers += 1

        session.current_index += 1

        self.session_repo.save(session)

        if session.current_index >= len(words):

            accuracy = int(
                session.correct_answers
                * 100
                / session.total_questions
            )

            return {
                "finished": True,
                "is_correct": is_correct,
                "correct_answer": current_word.russian,
                "correct_answers": session.correct_answers,
                "total_questions": session.total_questions,
                "accuracy": accuracy
            }

        next_word = words[
            session.current_index
        ]

        return {
            "finished": False,
            "is_correct": is_correct,
            "correct_answer": current_word.russian,
            "next_word": {
                "word_id": next_word.id,
                "english": next_word.english
            }
        }