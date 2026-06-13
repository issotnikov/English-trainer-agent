from uuid import UUID

from sqlalchemy.orm import Session

from app.models.training_session import TrainingSession


class TrainingRepository:

    def create(
        self,
        db: Session,
        session: TrainingSession
    ) -> TrainingSession:
        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    def get_by_id(
        self,
        db: Session,
        session_id: UUID
    ) -> TrainingSession | None:
        return (
            db.query(TrainingSession)
            .filter(
                TrainingSession.id == session_id
            )
            .first()
        )

    def get_by_id_and_user(
        self,
        db: Session,
        session_id: UUID,
        user_id: UUID
    ) -> TrainingSession | None:
        return (
            db.query(TrainingSession)
            .filter(
                TrainingSession.id == session_id,
                TrainingSession.user_id == user_id
            )
            .first()
        )

    def save(
        self,
        db: Session,
        session: TrainingSession
    ) -> TrainingSession:
        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    def delete(
        self,
        db: Session,
        session: TrainingSession
    ) -> None:
        db.delete(session)
        db.commit()


training_repository = TrainingRepository()