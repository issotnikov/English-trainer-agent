from pydantic import BaseModel


class TrainingStatsResponse(BaseModel):

    total_sessions: int
    total_questions: int
    correct_answers: int
    average_accuracy: int
    best_accuracy: int