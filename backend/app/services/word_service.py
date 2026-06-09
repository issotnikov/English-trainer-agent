from app.repositories.word_repository import WordRepository
class WordService:

    def __init__(self, repo: WordRepository):
        self.repo = repo

    def create_word(
        self,
        english: str,
        russian: str,
        user_id: str,
        category_id: str
    ):
        return self.repo.create(
            english=english,
            russian=russian,
            user_id=user_id,
            category_id=category_id
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

    def get_words_by_category(
        self,
       category_id: str
    ):
    
        return self.repo.get_by_category_id(
            category_id=category_id
        )

    def get_category_words(
        self,
        category_id: str,
        user_id: str
    ):
       return self.repo.get_by_category(
           category_id=category_id,
           user_id=user_id
        )