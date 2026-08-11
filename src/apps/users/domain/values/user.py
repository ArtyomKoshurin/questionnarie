from enum import Enum


class UserRole(Enum):
    author: str = "Автор опроса"
    participant: str = "Участник опроса"
