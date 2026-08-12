from enum import Enum


class UserRole(Enum):
    author: str = "Автор опроса"
    participant: str = "Участник опроса"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        return [(item.name, item.value) for item in cls]
