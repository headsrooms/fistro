import string
from contextlib import suppress
from dataclasses import make_dataclass
from typing import Type, Any, List, Tuple, Optional

from fistro.generators import str_generator



def is_list(type: Any) -> bool:
    try:
        return type._name == 'List' or type is list
    except AttributeError:
        return False


def is_dict(type: Any) -> bool:
    try:
        return type is dict or type._name == 'Dict'
    except AttributeError:
        return False


def get_base_type(type: Any) -> Type:
    if is_dict(type):
        return type.__args__[1]
    return type.__args__[0]


def valid_id() -> str:
    return str_generator(population=string.ascii_lowercase)


def spawn_class(class_name: str, fields: List[Tuple[Any, Any, Optional[Any]]]) -> None:
    the_class = make_dataclass(class_name, fields)
    globals()[class_name] = the_class

    return the_class
