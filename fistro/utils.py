import string
from dataclasses import make_dataclass
from inspect import signature
from typing import Type, Any, List, Tuple, Optional, Callable

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


def valid_id() -> str:
    return str_generator(population=string.ascii_lowercase)


def spawn_class(class_name: str, fields: List[Tuple[Any, Any, Optional[Any]]]) -> None:
    the_class = make_dataclass(class_name, fields)
    globals()[class_name] = the_class

    return the_class


def get_base_type(type: Any) -> Type:
    if is_dict(type):
        return type.__args__[1]
    return type.__args__[0]


def get_name(the_type: Type) -> str:
    return the_type.__qualname__


def get_return_type(generator: Callable) -> Type:
    return signature(generator).return_annotation


def get_return_type_name(generator: Callable) -> str:
    return_type = signature(generator).return_annotation
    try:
        return return_type.__qualname__
    except AttributeError:  # is a complex type: List or Dict
        if is_dict(return_type):
            return f'{get_base_type(return_type)}_dict'
        elif is_list(return_type):
            return f'{get_base_type(return_type)}_list'
