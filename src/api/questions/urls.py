from django.urls import path

from src.api.questions.handlers import QuestionView

urlpatterns = [
    path(
        "questionnaire/<uuid:questionnaire_uuid>/question/<int:order_number>/",
        QuestionView.as_view(),
        name="questionnaire-question",
    ),
]
