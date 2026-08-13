from django.urls import include, path

urlpatterns = [
    path("questions/", include("src.api.questions.urls")),
]
