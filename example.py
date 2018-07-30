from datetime import datetime

from fistro.fistro import generate
from fistro.generators import date_generator


class TestClassWithYDefault:
    x: int
    y: str = 'default'
    z: str = str(date_generator())
    w: datetime
    o: str


generated = generate(TestClassWithYDefault)()
print(generated)
