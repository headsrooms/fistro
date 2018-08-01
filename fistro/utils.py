from typing import Type, Any


def is_list(type: Any) -> bool:
    return type._name == 'List'


def get_base_type(type: Any) -> Type:
    return type.__args__[0]
