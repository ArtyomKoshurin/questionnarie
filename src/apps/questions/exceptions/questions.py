from dataclasses import dataclass

from src.apps.common.exceptions import ServiceException


@dataclass
class GetQuestionByOrderException(ServiceException):
    question: str

    @property
    def message(self):
        return f"Не удалось получить вопрос {self.question}."
