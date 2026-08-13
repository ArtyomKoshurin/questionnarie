from functools import lru_cache

import punq

from src.apps.questions.domain.interfaces.repos.questions import \
    BaseQuestionRepo
from src.apps.questions.repos.questions import QuestionRepo
from src.apps.questions.use_cases.questions import GetQuestionUseCase


@lru_cache(1)
def get_questions_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    container.register(BaseQuestionRepo, QuestionRepo)
    container.register(GetQuestionUseCase)

    return container
