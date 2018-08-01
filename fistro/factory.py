import builtins
from inspect import signature
from typing import Type, Callable, List

from fistro.config import supported_types
from fistro.exceptions import NotSupportedType
from fistro.generators import default_generators
from fistro.utils import is_list, get_base_type


def builtin_types() -> List:
    return [
        getattr(builtins, d)
        for d in dir(builtins)
        if isinstance(getattr(builtins, d), type)
    ]


class Factory:
    def __init__(self, generators: List[Callable] = default_generators()) -> None:
        for generator in generators:
            try:
                type_name = signature(generator).return_annotation.__name__
                setattr(self, f'{type_name}_generator', generator)
            except AttributeError:
                if is_list(signature(generator).return_annotation):
                    setattr(
                        self,
                        f'{get_base_type(signature(generator).return_annotation)}_list_generator',
                        generator,
                    )

    def factory(self, typename: Type) -> Callable:
        if typename in supported_types():
            try:
                return getattr(self, f'{typename.__name__}_generator')
            except AttributeError:  # this is to protect against the case of any type generator is not provided or is a complex type: List...
                if is_list(typename):
                    return getattr(self, f'{get_base_type(typename)}_list_generator')
                return getattr(DefaultFactory(), f'{typename.__name__}_generator')
        raise NotSupportedType(f'Type {typename} is not supported')


class DefaultFactory:
    def __init__(self):
        for generator in default_generators():
            type_name = signature(generator).return_annotation.__name__
            setattr(self, f'{type_name}_generator', generator)
