Fistro
======

.. image:: https://img.shields.io/pypi/v/fistro.svg
    :target: https://pypi.org/project/fistro/

.. image:: https://img.shields.io/pypi/pyversions/fistro.svg
    :target: https://pypi.org/project/fistro/

.. image:: https://img.shields.io/circleci/project/github/kingoodie/fistro.svg
    :target: https://circleci.com/gh/kingoodie/fistro

A fixture generator based on type annotations.

Examples
--------

>>> from datetime import datetime
>>>
>>> from fistro.fistro import generate
>>> from fistro.generators import date_generator
>>>
>>>
>>> class TestClassWithYDefault:
>>>     x: int
>>>     y: str = 'default'
>>>     z: str = str(date_generator())
>>>     w: datetime
>>>     o: str
>>>
>>>
>>> generated = generate(TestClassWithYDefault)()
>>> print(generated)


Installation
------------

>>> pip install poetry
>>> poetry install -v

If you were on a virtualenv, dependencies will be installed on this one,
otherwise a new virtualenv will be created and poetry will show you the path.

Another way is with:

>>> pip install -r requirements.txt

This way dev dependencies won't be installed.


Credits
--------
In memoriam of `Chiquito de la Calzada <https://es.wikipedia.org/wiki/Chiquito_de_la_Calzada>`_.