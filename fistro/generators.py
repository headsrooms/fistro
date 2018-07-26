from datetime import datetime


# Name is not important, the important thing is the return type
# if this one is repeated generator will be override


def int_generator() -> int:
    return 5


def str_generator() -> str:
    return 'A'


def date_generator() -> datetime:
    return datetime.strptime('26/07/2017', '%d/%m/%Y')
