from dataclasses import dataclass

from src.apps.common.dtos import BaseDTO
from src.apps.questions.domain.entities.questions import Answer, Question


@dataclass
class AnswerDTO(BaseDTO):
    text: str
    order_number: int

    @classmethod
    def from_entity(cls, entity: Answer) -> "AnswerDTO":
        return cls(
            uuid=entity.uuid,
            text=entity.text,
            order_number=entity.order_number,
        )


@dataclass
class QuestionDTO(BaseDTO):
    text: str
    answers: list[AnswerDTO]
    order_number: int

    @classmethod
    def from_entity(cls, entity: Question) -> "QuestionDTO":
        return cls(
            uuid=entity.uuid,
            text=entity.text,
            answers=[AnswerDTO.from_entity(answer) for answer in entity.answers],
            order_number=entity.order_number,
        )
