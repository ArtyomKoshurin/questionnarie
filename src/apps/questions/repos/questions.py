from src.apps.questions.domain.entities.questions import Question
from src.apps.questions.domain.interfaces.repos.questions import \
    BaseQuestionRepo
from src.apps.questions.exceptions.questions import GetQuestionByOrderException


class QuestionRepo(BaseQuestionRepo):

    def get_one(self, uuid: str) -> Question:
        ...

    def get_by_questionnaire_and_order(self, questionnaire_uuid: str, order_number: int):
        try:
            ...

        except Exception:
            raise GetQuestionByOrderException(question=order_number)
