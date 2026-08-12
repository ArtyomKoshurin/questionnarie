from dataclasses import dataclass

from src.apps.common.entities import BaseEntity
from src.apps.users.domain.values.user import UserRole


@dataclass
class User(BaseEntity):
    username: str
    email: str
    role: UserRole
