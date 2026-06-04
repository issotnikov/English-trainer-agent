from app.repositories.word_repository import WordRepository


class WordService:

    def __init__(self, repo: WordRepository):
        self.repo = repo

    def create_word(
        self,
        english: str,
        russian: str,
        user_id: str
    ):
        return self.repo.create(
            english=english,
            russian=russian,
            user_id=user_id
        )

    def get_user_words(
        self,
        user_id: str
    ):
        return self.repo.get_by_user_id(
            user_id=user_id
        )

    def delete_word(
        self,
        word_id: str,
        user_id: str
    ):
        return self.repo.delete(
            word_id=word_id,
            user_id=user_id
        )