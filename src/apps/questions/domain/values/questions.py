from enum import Enum


class QuestionnaireStatus(Enum):
    in_progress: str = "В процессе"
    completed: str = "Пройден"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(item.name, item.value) for item in cls]
