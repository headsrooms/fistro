import json
from dataclasses import make_dataclass, field, asdict
from typing import Type, Optional, List, Callable

from fistro.factory import Factory


def generate(
    a_class: Type,
    generators: Optional[List[Callable]] = None,
    as_dict: bool = False,
    as_json: bool = False,
) -> Type:
    annotations = a_class.__annotations__
    defaults = []

    for field_name in annotations.keys():
        try:
            defaults.append(getattr(a_class, field_name))
        except AttributeError:
            defaults.append(None)

    rich_annotations = [
        (
            name,
            typename,
            field(
                default_factory=Factory().factory(typename)
                if not generators
                else Factory(generators).factory(typename)
            )
            if not defaults[i]
            else field(default=defaults[i]),
        )
        for i, (name, typename) in enumerate(annotations.items())
    ]

    dataclass = make_dataclass(a_class.__name__, rich_annotations)
    if as_dict:
        return asdict(
            dataclass()
        )  # to make asdict parameter must be an instance of dataclass
    if as_json:
        return json.dumps(asdict(dataclass()))
    return dataclass
