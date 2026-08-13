from django.contrib import admin

from src.apps.questions.models.questions import (AnswerModel, QuestionModel,
                                                 QuestionnaireModel)


@admin.register(QuestionnaireModel)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ["uuid", "author", "name", "creation_date"]
    search_fields = ("uuid", "name")
    readonly_fields = ("uuid",)
    list_select_related = ("author",)

    def author(self, obj):
        return obj.author.username

    author.short_description = "Автор"


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["uuid", "questionnaire", "text", "order_number"]
    search_fields = ("uuid",)
    readonly_fields = ("uuid",)
    list_select_related = ("questionnaire",)

    def questionnaire(self, obj):
        return obj.questionnaire.name

    questionnaire.short_description = "Опросник"


@admin.register(AnswerModel)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["uuid", "question", "questionnaire", "text", "order_number"]
    search_fields = ("uuid",)
    readonly_fields = ("uuid",)
    list_select_related = ("question",)

    def question(self, obj):
        return obj.question.order_number

    def questionnaire(self, obj):
        return obj.question.questionnaire.name

    question.short_description = "Номер вопроса"
    questionnaire.short_description = "Опросник"
