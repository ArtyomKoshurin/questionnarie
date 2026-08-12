from uuid import uuid4

from django.db import models


class AddUUIDModel(models.Model):
    uuid = models.CharField(max_length=255, default=uuid4, unique=True, verbose_name="Уникальный идентификатор")

    class Meta:
        abstract = True
