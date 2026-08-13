from rest_framework import serializers

from src.apps.questions.dtos.questions import AnswerDTO, QuestionDTO


class AnswerOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    text = serializers.CharField()
    order_number = serializers.IntegerField()

    def to_representation(self, dto: AnswerDTO) -> dict:
        return {
            "uuid": dto.uuid,
            "text": dto.text,
            "order_number": dto.order_number,
        }


class QuestionOutputSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    text = serializers.CharField()
    order_number = serializers.IntegerField()
    answers = AnswerOutputSerializer(many=True)

    def to_representation(self, dto: QuestionDTO) -> dict:
        return {
            "uuid": dto.uuid,
            "text": dto.text,
            "order_number": dto.order_number,
            "answers": self.fields["answers"].to_representation(dto.answers),
        }
