import json
from dataclasses import make_dataclass, field, asdict, fields, MISSING
from typing import Optional, List, Callable, Any, Union, Dict, Tuple

from fistro.factory import Factory


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
        print({key: inner_inspection(value) for key, value in object.items()})
    elif isinstance(object, list):
        print([inner_inspection(value) for value in object])


def inner_inspection(inner_object: Any):
    if isinstance(inner_object, list):
        for value in inner_object:
            if isinstance(value, list):
                # return [type(inner_value) for inner_value in value]
                return [inner_inspection(inner_value) for inner_value in value]
            elif isinstance(value, dict):
                # return {inner_key: type(inner_value) for inner_key, inner_value in value.items()}
                return {
                    inner_key: inner_inspection(inner_value)
                    for inner_key, inner_value in value.items()
                }
        return [type(value) for value in inner_object]
    elif isinstance(inner_object, dict):
        for value in inner_object:
            if isinstance(value, list):
                return [inner_inspection(inner_value) for inner_value in value]
            elif isinstance(value, dict):
                return {
                    inner_key: inner_inspection(inner_value)
                    for inner_key, inner_value in value.items()
                }
    else:
        return type(inner_object)
