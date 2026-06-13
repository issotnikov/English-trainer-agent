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
        category_id: str | None = None
    ) -> TrainingSession:

        session = TrainingSession(
            user_id=user_id,
            category_id=category_id,
            total_questions=total_questions
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