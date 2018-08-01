import json
from dataclasses import make_dataclass, field, asdict, fields, MISSING
from typing import Optional, List, Callable, Any, Tuple

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
