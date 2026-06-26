import json
import random

from datetime import datetime
from datetime import timedelta

from app.repositories.word_repository import (
    WordRepository
)

from app.repositories.training_session_repository import (
    TrainingSessionRepository
)

REVIEW_INTERVALS = {
    0: 1,
    1: 3,
    2: 7,
    3: 14,
    4: 30,
    5: 60,
    6: 90
}

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

            words = [
                word
                for word in words
                if (
                    word.next_review_at is None
                    or
                    word.next_review_at <= datetime.utcnow()
                )
            ]

        else:

            words = (
                self.word_repo
                .get_words_for_review(
                    user_id=user_id
                )   
            )

        if not words:
            return None

        word_ids = [
            str(word.id)
            for word in words
        ]

        random.shuffle(word_ids)

        session = self.session_repo.create(
            user_id=user_id,
            category_id=category_id,
            total_questions=len(words),
            word_order=json.dumps(word_ids)
        )

        first_word_id = word_ids[0]

        first_word = next(
            word
            for word in words
            if str(word.id) == first_word_id
        )

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

        word_order = json.loads(
           session.word_order
        )

        words_map = {
            str(word.id): word
            for word in words
        }

        if session.current_index >= len(word_order):
            return None

        current_word_id = word_order[
            session.current_index
        ]

        current_word = words_map[
            current_word_id
        ]

        is_correct = (
            answer.strip().lower()
            ==
            current_word.russian.strip().lower()
        )

        self.word_repo.update_training_result(
            word=current_word,
            is_correct=is_correct
        )

        if is_correct:
            session.correct_answers += 1

        session.current_index += 1

        self.session_repo.save(session)

        if session.current_index >= len(word_order):

            from datetime import datetime

            session.is_completed = True

            session.completed_at = datetime.utcnow()

            self.session_repo.save(session)

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

        next_word_id = word_order[
            session.current_index
        ]

        next_word = words_map[
            next_word_id
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

    def get_history(
        self,
        user_id: str
    ):

        sessions = (
            self.session_repo
            .get_user_history(user_id)
        )

        result = []

        for session in sessions:

            accuracy = int(
                session.correct_answers
                * 100
                / session.total_questions
            )

            result.append(
                {
                    "session_id": session.id,
                    "created_at": session.created_at,
                    "completed_at": session.completed_at,
                    "correct_answers": session.correct_answers,
                    "total_questions": session.total_questions,
                    "accuracy": accuracy
                }
            )

        return result

    def get_stats(
        self,
        user_id: str
    ):

        sessions = (
            self.session_repo
            .get_completed_sessions(
                user_id
            )
        )

        if not sessions:

            return {
                "total_sessions": 0,
                "total_questions": 0,
                "correct_answers": 0,
                "average_accuracy": 0,
                "best_accuracy": 0
            }

        total_sessions = len(
            sessions
        )

        total_questions = sum(
            s.total_questions
            for s in sessions
        )

        correct_answers = sum(
            s.correct_answers
            for s in sessions
        )

        accuracies = [
            int(
                s.correct_answers
                * 100
                / s.total_questions
            )
            for s in sessions
        ]

        average_accuracy = int(
            sum(accuracies)
            / len(accuracies)
        )

        best_accuracy = max(
            accuracies
        )

        return {
            "total_sessions": total_sessions,
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "average_accuracy": average_accuracy,
            "best_accuracy": best_accuracy
        }
    
    def get_word_progress(
        self,
        user_id: str
    ):

        words = self.word_repo.get_progress(
        user_id
        )

        result = []

        for word in words:

            total = (
                word.correct_answers
                +
                word.wrong_answers
            )

            accuracy = (
                int(
                    word.correct_answers
                    * 100
                    / total
                )
                if total > 0
                else 0
            )

            result.append(
                {
                    "word_id": word.id,
                    "english": word.english,
                    "correct_answers": word.correct_answers,
                    "wrong_answers": word.wrong_answers,
                    "accuracy": accuracy,
                    "last_trained_at": word.last_trained_at
                }
            )

        return result

    def get_hard_words(
        self,
        user_id: str
    ):

        words = (
            self.word_repo
            .get_hard_words(user_id)
        )

        result = []

        for word in words:

            result.append(
                {
                    "word_id": word.id,
                    "english": word.english,
                    "russian": word.russian,
                    "difficulty": word.difficulty,
                    "correct_answers": (
                        word.correct_answers
                    ),
                    "wrong_answers": (
                        word.wrong_answers
                    ),
                    "repetition_level": (
                        word.repetition_level
                    ),
                    "next_review_at": (
                        word.next_review_at
                    )
                }
            )

        return result