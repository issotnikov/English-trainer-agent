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

    def export_words(
        self,
        user_id: str
    ):

        words = self.repo.export_words(
            user_id=user_id
        )

        result = []

        for word in words:

            result.append(
                {
                    "id": word.id,
                    "english": word.english,
                    "russian": word.russian,
                    "category_id": word.category_id,
                    "correct_answers": word.correct_answers,
                    "wrong_answers": word.wrong_answers,
                    "difficulty": word.difficulty,
                    "repetition_level": word.repetition_level,
                    "next_review_at": word.next_review_at,
                    "last_trained_at": word.last_trained_at
                }
            )

        return result

    def import_words(
        self,
        words: list,
        user_id: str
    ):

        imported = 0
        skipped = 0

        for item in words:

            if self.repo.exists(
                english=item.english,
                user_id=user_id
            ):
                skipped += 1
                continue

            self.repo.create(
                english=item.english,
                russian=item.russian,
                user_id=user_id,
                category_id=item.category_id
            )

            imported += 1

        return {
            "imported": imported,
            "skipped": skipped
        }