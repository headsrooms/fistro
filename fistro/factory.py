import builtins
from inspect import signature
from typing import Type, Callable, List

from fistro.config import supported_types
from fistro.exceptions import NotSupportedType
from fistro.generators import default_generators


def builtin_types() -> List:
    return [
        getattr(builtins, d)
        for d in dir(builtins)
        if isinstance(getattr(builtins, d), type)
    ]


class Factory:
    def __init__(self, generators: List[Callable] = default_generators()) -> None:
        for generator in generators:
            type_name = signature(generator).return_annotation.__name__
            setattr(self, f'{type_name}_generator', generator)

    def factory(self, typename: Type) -> Callable:
        if typename in supported_types():
            try:
                return getattr(self, f'{typename.__name__}_generator')
            except AttributeError:  # this is to protect against the case of some type generator is not provided
                return getattr(DefaultFactory(), f'{typename.__name__}_generator')
        raise NotSupportedType(f'Type {typename} is not supported')


class DefaultFactory:
    def __init__(self):
        for generator in default_generators():
            type_name = signature(generator).return_annotation.__name__
            setattr(self, f'{type_name}_generator', generator)
