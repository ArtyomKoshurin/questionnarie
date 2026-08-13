from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.questions.serializers import QuestionOutputSerializer
from src.apps.questions.use_cases.questions import GetQuestionUseCase
from src.project.containers.questions import get_questions_container


class QuestionView(APIView):

    def get(self, request, questionnaire_uuid: str, order_number: int):
        container = get_questions_container()
        use_case = container.resolve(GetQuestionUseCase)

        question = use_case.execute(
            questionnaire_uuid=questionnaire_uuid,
            order_number=order_number,
        )
        serializer = QuestionOutputSerializer(question)

        return Response(serializer.data, status=status.HTTP_200_OK)
