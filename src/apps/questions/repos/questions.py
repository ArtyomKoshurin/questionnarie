from src.apps.questions.domain.entities.questions import Question
from src.apps.questions.domain.interfaces.repos.questions import \
    BaseQuestionRepo
from src.apps.questions.exceptions.questions import GetQuestionByOrderException
from src.apps.questions.models.questions import QuestionModel


class QuestionRepo(BaseQuestionRepo):

    def get_one(self, uuid: str) -> Question:
        ...

    def get_by_questionnaire_and_order(self, questionnaire_uuid: str, order_number: int):
        try:
            obj = QuestionModel.objects.get(questionnaire__uuid=questionnaire_uuid, order_number=order_number)
            return obj.to_entity()

        except Exception:
            raise GetQuestionByOrderException(question=order_number)
