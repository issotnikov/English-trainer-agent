from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        name: str,
        user_id: str
    ) -> Category:

        category = Category(
            name=name,
            user_id=user_id
        )

        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def get_by_user_id(
        self,
        user_id: str
    ) -> list[Category]:

        return (
            self.db.query(Category)
            .filter(
                Category.user_id == user_id
            )
            .all()
        )

    def delete(
        self,
        category_id: str,
        user_id: str
    ) -> bool:

        category = (
            self.db.query(Category)
            .filter(
                Category.id == category_id,
                Category.user_id == user_id
            )
            .first()
        )

        if not category:
            return False

        self.db.delete(category)
        self.db.commit()

        return True