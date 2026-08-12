from django.db import models

from src.apps.common.models import AddUUIDModel
from src.apps.questions.domain.entities.questions import (Answer, Question,
                                                          Questionnaire)
from src.apps.users.models.user import CustomUser


class QuestionnaireModel(AddUUIDModel):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="questionnaires",
        verbose_name="Автор",
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def to_entity(self) -> Questionnaire:
        return Questionnaire(
            uuid=self.uuid,
            author=self.author.to_entity(),
            name=self.name,
            creation_date=self.creation_date,
            questions=[obj.to_entity() for obj in self.questions.all()],
        )

    def __str__(self):
        return f"Опросник {self.name} автора {self.author.username}"

    class Meta:
        verbose_name = "Опросник"
        verbose_name_plural = "Опросники"


class QuestionModel(AddUUIDModel):
    text = models.TextField(max_length=1024, verbose_name="Текст")
    questionnaire = models.ForeignKey(
        QuestionnaireModel,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Опросник",
    )
    order_number = models.IntegerField(verbose_name="Порядковый номер")

    def to_entity(self) -> Question:
        return Question(
            uuid=self.uuid,
            text=self.text,
            answers=[obj.to_entity() for obj in self.answers.all()],
            order_number=self.order_number,
        )

    def __str__(self):
        return f"Вопрос {self.order_number} опросника {self.questionnaire.name}"

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class AnswerModel(AddUUIDModel):
    text = models.TextField(max_length=1024, verbose_name="Текст")
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name="Вопрос",
    )
    order_number = models.IntegerField(verbose_name="Порядковый номер")

    def to_entity(self) -> Answer:
        return Answer(
            uuid=self.uuid,
            text=self.text,
            order_number=self.order_number,
        )

    def __str__(self):
        return (
            f"Ответ {self.order_number} вопроса {self.question.order_number} "
            f"вопросника {self.question.questionnaire.name}",
        )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
