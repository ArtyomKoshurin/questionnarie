from dataclasses import dataclass

from src.apps.questions.domain.interfaces.repos.questions import \
    BaseQuestionRepo
from src.apps.questions.dtos.questions import QuestionDTO


@dataclass
class GetQuestionUseCase:
    question_repo: BaseQuestionRepo

    def execute(self, questionnaire_uuid: str, order_number: int) -> QuestionDTO:
        question = self.question_repo.get_by_questionnaire_and_order(
            questionnaire_uuid=questionnaire_uuid, order_number=order_number,
        )

        return QuestionDTO.from_entity(question)
