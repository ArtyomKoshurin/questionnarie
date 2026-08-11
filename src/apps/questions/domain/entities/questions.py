from dataclasses import dataclass, field
from datetime import datetime

from src.apps.common.entities import BaseEntity
from src.apps.questions.domain.values.questions import QuestionnaireStatus
from src.apps.users.domain.entities.user import User


@dataclass
class Answer(BaseEntity):
    text: str
    order_number: int


@dataclass
class Question(BaseEntity):
    text: str
    answers: list[Answer]
    order_number: int


@dataclass
class Questionnaire(BaseEntity):
    author: User
    name: str
    creation_date: datetime
    questions: list[Question]


@dataclass
class QuestionnaireStatistic(BaseEntity):
    questionnaire: Questionnaire
    participant: User
    started_at: datetime
    status: QuestionnaireStatus = field(default=QuestionnaireStatus.in_progress)
    finished_at: datetime | None = field(default=None)
