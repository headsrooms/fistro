import json
from dataclasses import is_dataclass
from datetime import datetime

import pytest

from fistro import __version__
from fistro.exceptions import NotSupportedType
from fistro.fistro import generate
from fistro.generators import int_generator


class TestClass:
    x: int
    y: str


class TestClassWithNoSupportedType:
    x: int
    y: str
    z: float


class TestClassWithYDefault:
    x: int
    y: str = 'default'
    z: datetime


def override_str_generator() -> str:
    return 'override'


def override_int_generator() -> int:
    return 23


def test_version():
    assert __version__ == '0.1.0'


def test_simple():
    generated = generate(TestClassWithYDefault)()
    assert generated.y == TestClassWithYDefault.y  # default value provided
    assert (
        generated.x != int_generator()
    )  # no default value provided, so it will use the generator


def test_not_supported_type():
    with pytest.raises(NotSupportedType):
        generate(TestClassWithNoSupportedType)()


def test_complete_override_generators():
    override = generate(
        TestClass, generators=[override_int_generator, override_str_generator]
    )()
    assert override.x == override_int_generator()
    assert override.y == override_str_generator()


def test_partial_override_generator():
    override = generate(TestClass, generators=[override_str_generator])()
    assert override.x != int_generator()
    assert override.y == override_str_generator()


def test_is_dataclass():
    dataclass = generate(
        TestClass, generators=[override_int_generator, override_str_generator]
    )()

    assert is_dataclass(dataclass)


def test_as_dict():
    dataclass_dict = generate(
        TestClass, generators=[override_int_generator, override_str_generator], as_dict=True
    )
    assert dataclass_dict == {'x': 23, 'y': 'override'}


def test_as_json():
    dataclass_json = generate(
        TestClass, generators=[override_int_generator, override_str_generator], as_json=True
    )
    assert dataclass_json == json.dumps({'x': 23, 'y': 'override'})
