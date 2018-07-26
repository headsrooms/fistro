from datetime import datetime
from typing import List, Callable

from fistro.generators import int_generator, str_generator, date_generator


def supported_types() -> List:
    return [int, str, datetime]


def default_generators() -> List[Callable]:
    return [int_generator, str_generator, date_generator]
