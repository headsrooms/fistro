import string
from datetime import datetime, date
from random import randint, choices, choice
from typing import Dict, Optional, Callable, List

from fistro.config import (
    MIN_YEAR,
    MAX_YEAR,
    MIN_MONTH,
    MAX_MONTH,
    MIN_DAY,
    MAX_DAY,
    MIN_HOUR,
    MAX_HOUR,
    MIN_MINUTE,
    MAX_MINUTE,
    MIN_SECOND,
    MAX_SECOND,
    STR_LENGTH,
    INT_LENGTH,
    INT_LIST_LENGTH,
)


# Name is not important, the important thing is the return type
# if this one is repeated generator will be override

def int_generator(length: int = INT_LENGTH) -> int:
    return randint(0, 9 * 10 ** length)


def bool_generator() -> bool:
    return choice([True, False])


def str_generator(population: str = string.printable, length: int = STR_LENGTH) -> str:
    return ''.join(choices(population, k=length))


def datetime_generator(rand_date: Optional[Dict[str, int]] = None) -> datetime:
    if not rand_date:
        rand_date = {}
    min_year = rand_date.get('min_year', MIN_YEAR)
    max_year = rand_date.get('max_year', MAX_YEAR)
    min_month = rand_date.get('min_month', MIN_MONTH)
    max_month = rand_date.get('max_month', MAX_MONTH)
    min_day = rand_date.get('min_day', MIN_DAY)
    max_day = rand_date.get('max_day', MAX_DAY)
    min_hour = rand_date.get('min_hour', MIN_HOUR)
    max_hour = rand_date.get('max_hour', MAX_HOUR)
    min_minute = rand_date.get('min_minute', MIN_MINUTE)
    max_minute = rand_date.get('max_minute', MAX_MINUTE)
    min_second = rand_date.get('min_second', MIN_SECOND)
    max_second = rand_date.get('max_second', MAX_SECOND)

    year = randint(min_year, max_year)
    month = randint(min_month, max_month)
    day = randint(min_day, max_day)
    hour = randint(min_hour, max_hour)
    minute = randint(min_minute, max_minute)
    second = randint(min_second, max_second)
    the_date = datetime(
        year=year, month=month, day=day, hour=hour, minute=minute, second=second
    )
    return datetime.strptime(str(the_date), '%Y-%m-%d %H:%M:%S')


def date_generator(rand_date: Optional[Dict[str, int]] = None) -> date:
    if not rand_date:
        rand_date = {}
    min_year = rand_date.get('min_year', MIN_YEAR)
    max_year = rand_date.get('max_year', MAX_YEAR)
    min_month = rand_date.get('min_month', MIN_MONTH)
    max_month = rand_date.get('max_month', MAX_MONTH)
    min_day = rand_date.get('min_day', MIN_DAY)
    max_day = rand_date.get('max_day', MAX_DAY)

    year = randint(min_year, max_year)
    month = randint(min_month, max_month)
    day = randint(min_day, max_day)

    the_date = date(year=year, month=month, day=day)
    return datetime.strptime(str(the_date), '%Y-%m-%d').date()


def int_list_generator(
    list_length: int = INT_LIST_LENGTH, int_length: int = INT_LENGTH
) -> List[int]:
    return [randint(0, 9 * 10 ** int_length) for _ in range(list_length)]


def int_dict_generator(
    dict_length: int = INT_LIST_LENGTH, int_length: int = INT_LENGTH
) -> Dict[str, int]:
    return {
        str_generator(): randint(0, 9 * 10 ** int_length) for _ in range(dict_length)
    }


def default_generators() -> List[Callable]:
    return [
        int_generator,
        bool_generator,
        str_generator,
        datetime_generator,
        date_generator,
        int_list_generator,
        int_dict_generator,
    ]
