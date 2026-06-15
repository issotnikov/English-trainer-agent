from app.models.training_session import (
    TrainingSession
)


class TrainingSessionRepository:

    def __init__(self, db):
        self.db = db

    def create(
        self,
        user_id: str,
        total_questions: int,
        category_id: str | None = None,
        word_order: str = "[]"
    ) -> TrainingSession:

        session = TrainingSession(
            user_id=user_id,
            category_id=category_id,
            total_questions=total_questions,
            word_order=word_order
        )

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def get_by_id(
        self,
        session_id: str
    ) -> TrainingSession | None:

        return (
            self.db.query(TrainingSession)
            .filter(
                TrainingSession.id == session_id
            )
            .first()
        )

    def save(
        self,
        session: TrainingSession
    ) -> TrainingSession:

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session

    def get_user_history(
        self,
        user_id: str
    ):

        return (
            self.db.query(
                TrainingSession
            )
            .filter(
                TrainingSession.user_id == user_id,
                TrainingSession.is_completed == True
            )
            .order_by(
                TrainingSession.created_at.desc()
            )
            .all()
        )

    def get_completed_sessions(
        self,
        user_id: str
    ):

        return (
            self.db.query(
                TrainingSession
            )
            .filter(
                TrainingSession.user_id == user_id,
                TrainingSession.is_completed == True
            )
            .all()
        )