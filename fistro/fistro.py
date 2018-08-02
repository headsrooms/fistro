import json
from dataclasses import make_dataclass, field, asdict, fields, MISSING
from typing import Optional, List, Callable, Any, Union, Dict, Tuple

from fistro.factory import Factory
from fistro.utils import valid_id


def generate(
    a_class: Any,
    generators: Optional[List[Callable]] = None,
    as_dict: bool = False,
    as_json: bool = False,
) -> Any:  # really Union[Type[Any], str, Dict[Any, Any]] but mypy is complaining

    rich_fields = enrich_fields(a_class, generators)

    dataclass = make_dataclass(a_class.__name__, rich_fields)
    if as_dict:
        return asdict(
            dataclass()
        )  # to make asdict parameter must be an instance of dataclass
    if as_json:
        return json.dumps(asdict(dataclass()))
    return dataclass


def enrich_fields(a_class, generators) -> List[Tuple[str, type, field]]:
    return [
        (
            a_field.name,
            a_field.type,
            field(
                default_factory=Factory().factory(a_field.type)
                if not generators
                else Factory(generators).factory(a_field.type)
            )
            if a_field.default is MISSING
            else field(default=a_field.default),
        )
        for a_field in fields(a_class)
    ]


def generate_from_json(object: Union[Dict[str, Any], List]):
    if isinstance(object, dict):
        return make_dataclass(
            valid_id(),
            [(key, *inner_inspection(value)) for key, value in object.items()],
        )
    raise NotImplemented('This case makes no much sense')


def inner_inspection(inner_object: Any):
    if isinstance(inner_object, dict):
        a_key = next(iter(inner_object.keys()))
        a_value = inner_object[a_key]
        inner_type = Dict[type(a_key), type(a_value)]

    elif isinstance(inner_object, list):
        inner_type = List[type(inner_object[0])]
    else:
        inner_type = type(inner_object)

    # using default factory we can reuse the field and auto-generate similar objects,
    # with default derived objects would be with this field constant
    return inner_type, field(default_factory=lambda: inner_object)
