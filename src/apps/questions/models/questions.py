from django.db import models

from src.apps.common.models import AddUUIDModel
from src.apps.questions.domain.entities.questions import (
    Answer, Question, QuestionAnswer, Questionnaire, QuestionnaireCompletion)
from src.apps.questions.domain.values.questions import QuestionnaireStatus
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
        unique_together = [("questionnaire", "order_number")]
        ordering = ["order_number"]


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
            f"опроса {self.question.questionnaire.name}",
        )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        unique_together = [("question", "order_number")]
        ordering = ["order_number"]


class QuestionnaireCompletionModel(AddUUIDModel):
    questionnaire = models.ForeignKey(
        QuestionnaireModel,
        on_delete=models.CASCADE,
        related_name="questionnaire_completions",
        verbose_name="Опросник",
    )
    participant = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="questionnaire_completions",
        verbose_name="Участник",
    )
    status = models.CharField(
        choices=QuestionnaireStatus.choices(),
        default=QuestionnaireStatus.in_progress,
        verbose_name="Статус прохождения",
    )
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала прохождения")
    finished_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата окончания прохождения")

    def to_entity(self) -> QuestionnaireCompletion:
        return QuestionnaireCompletion(
            uuid=self.uuid,
            questionnaire=self.questionnaire.to_entity(),
            participant=self.participant.to_entity(),
            started_at=self.started_at,
            finished_at=self.finished_at,
            status=QuestionnaireStatus[self.status],
            user_answers=[obj.to_entity() for obj in self.user_answers.all()],
        )

    def __str__(self):
        return f"Информация о прохождении опроса {self.questionnaire.name} пользователем {self.participant.username}"

    class Meta:
        verbose_name = "Информация о прохождении опроса"
        verbose_name_plural = "Информация о прохождении опросов"


class QuestionAnswerModel(AddUUIDModel):
    completion = models.ForeignKey(
        QuestionnaireCompletionModel,
        on_delete=models.CASCADE,
        related_name="user_answers",
        verbose_name="Информация о прохождении",
    )
    question = models.ForeignKey(
        QuestionModel,
        on_delete=models.CASCADE,
        related_name="user_answers",
        verbose_name="Вопрос",
    )
    selected_answer = models.ForeignKey(
        AnswerModel,
        on_delete=models.CASCADE,
        related_name="user_answers",
        verbose_name="Ответ",
    )

    def to_entity(self) -> QuestionAnswer:
        return QuestionAnswer(
            uuid=self.uuid,
            question=self.question.to_entity(),
            selected_answer=self.selected_answer.to_entity(),
        )

    def __str__(self):
        return (
            f"Выбранный ответ {self.selected_answer.order_number} на вопрос {self.question} "
            f"опросника {self.question.questionnaire.name}"
        )

    class Meta:
        verbose_name = "Выбранный ответ на вопрос"
        verbose_name_plural = "Выбранные ответы на вопросы"
