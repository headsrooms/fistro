from datetime import datetime, date
from typing import FrozenSet

INT_LENGTH = 9
STR_LENGTH = 9

MIN_YEAR = 0
MAX_YEAR = 2200
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
MIN_HOUR = 0
MAX_HOUR = 23
MIN_MINUTE = 0
MAX_MINUTE = 59
MIN_SECOND = 1
MAX_SECOND = 59


def supported_types() -> FrozenSet:
    return frozenset([int, str, datetime, date])
