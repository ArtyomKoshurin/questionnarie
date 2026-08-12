from abc import ABC, abstractmethod

from src.apps.questions.domain.entities.questions import Question


class BaseQuestionRepo(ABC):

    @abstractmethod
    def get_one(self, uuid: str) -> Question:
        ...

    @abstractmethod
    def get_by_questionnaire_and_order(self, questionnaire_uuid: str, order_number: int) -> Question:
        ...
