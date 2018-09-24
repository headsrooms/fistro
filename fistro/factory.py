import builtins
from inspect import signature
from typing import Type, Callable, List

from fistro.config import supported_types
from fistro.exceptions import NotSupportedType
from fistro.generators import default_generators
from fistro.utils import (
    is_list,
    get_base_type,
    is_dict,
    get_name,
    get_return_type,
    get_return_type_name,
)


def builtin_types() -> List:
    return [
        getattr(builtins, d)
        for d in dir(builtins)
        if isinstance(getattr(builtins, d), type)
    ]


class Factory:
    def __init__(self, generators: List[Callable] = None) -> None:
        if not generators:
            generators = default_generators()

        for generator in generators:
            try:
                type_name = get_return_type_name(generator)
                setattr(self, f'{type_name}_generator', generator)
            except AttributeError:
                if is_dict(signature(generator).return_annotation):
                    setattr(
                        self,
                        f'{get_base_type(get_return_type(generator))}_dict_generator',
                        generator,
                    )
                elif is_list(signature(generator).return_annotation):
                    setattr(
                        self,
                        f'{get_base_type(get_return_type(generator))}_list_generator',
                        generator,
                    )

    def factory(self, the_type: Type) -> Callable:
        if the_type in supported_types():
            try:
                return getattr(self, f'{get_name(the_type)}_generator')
            except AttributeError:
                # this is to protect against the case of any type generator is
                # not provided or is a complex type: List...
                if is_dict(the_type):
                    return getattr(self, f'{get_base_type(the_type)}_dict_generator')
                elif is_list(the_type):
                    return getattr(self, f'{get_base_type(the_type)}_list_generator')
                return getattr(
                    DefaultFactory(), f'{get_name(the_type)}_generator'
                )  # generator for this type is not setup
        raise NotSupportedType(f'Type {the_type} is not supported')


class DefaultFactory:
    def __init__(self):
        for generator in default_generators():
            type_name = get_return_type_name(generator)
            setattr(self, f'{type_name}_generator', generator)
