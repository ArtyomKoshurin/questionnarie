from functools import lru_cache

import punq


@lru_cache(1)
def get_questions_container() -> punq.Container:
    return _initialize_container


def _initialize_container() -> punq.Container:
    punq.Container()
