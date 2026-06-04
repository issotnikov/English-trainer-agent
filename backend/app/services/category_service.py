from app.repositories.category_repository import (
    CategoryRepository
)


class CategoryService:

    def __init__(
        self,
        repo: CategoryRepository
    ):
        self.repo = repo

    def create_category(
        self,
        name: str,
        user_id: str
    ):
        return self.repo.create(
            name=name,
            user_id=user_id
        )

    def get_user_categories(
        self,
        user_id: str
    ):
        return self.repo.get_by_user_id(
            user_id=user_id
        )

    def delete_category(
        self,
        category_id: str,
        user_id: str
    ):
        return self.repo.delete(
            category_id=category_id,
            user_id=user_id
        )