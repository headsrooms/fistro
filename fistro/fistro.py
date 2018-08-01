import json
import string
from dataclasses import make_dataclass, field, asdict, fields, MISSING
from typing import Optional, List, Callable, Any, Union, Dict, Tuple
from uuid import uuid4

from fistro.factory import Factory
from fistro.generators import str_generator


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


def valid_id() -> str:
    return str_generator(population=string.ascii_lowercase)


def generate_from_json(object: Union[Dict[str, Any], List]):
    if isinstance(object, dict):
        return make_dataclass(
            valid_id(),
            [(key, inner_inspection(value)) for key, value in object.items()],
        )
    elif isinstance(object, list):
        inner_type = inner_inspection(object[0])
        return generate(make_dataclass(valid_id(), [(valid_id(), List[inner_type])]))


def inner_inspection(inner_object: Any):
    if isinstance(inner_object, dict):
        for value in inner_object:
            if isinstance(value, list):
                return [inner_inspection(inner_value) for inner_value in value]
            elif isinstance(value, dict):
                return {
                    inner_key: inner_inspection(inner_value)
                    for inner_key, inner_value in value.items()
                }
    elif isinstance(inner_object, list):
        for value in inner_object:
            if isinstance(value, list):
                return make_dataclass(
                    str(uuid4()),
                    [(List[inner_inspection(inner_value)]) for inner_value in value],
                )
            elif isinstance(value, dict):
                return make_dataclass(
                    str(uuid4()),
                    [
                        inner_inspection(inner_value)
                        for inner_key, inner_value in value.items()
                    ],
                )
        return [type(value) for value in inner_object]
    return type(inner_object)
