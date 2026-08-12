from django.contrib.auth.models import AbstractUser
from django.db import models

from src.apps.common.models import AddUUIDModel
from src.apps.users.domain.entities.user import User
from src.apps.users.domain.values.user import UserRole


class CustomUser(AddUUIDModel, AbstractUser):
    role = models.CharField(choices=UserRole.choices(), verbose_name="Роль")

    def to_entity(self) -> User:
        return User(
            uuid=self.uuid,
            username=self.username,
            email=self.email,
            role=UserRole[self.role],
        )

    def __str__(self) -> str:
        return f"Пользователь {self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
