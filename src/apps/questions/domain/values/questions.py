from enum import Enum


class QuestionnaireStatus(Enum):
    in_progress: str = "В процессе"
    completed: str = "Пройден"
