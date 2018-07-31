Fistro
======

.. image:: https://img.shields.io/pypi/v/fistro.svg
    :target: https://pypi.org/project/fistro/

.. image:: https://img.shields.io/pypi/pyversions/fistro.svg
    :target: https://pypi.org/project/fistro/

.. image:: https://img.shields.io/circleci/project/github/kingoodie/fistro.svg
    :target: https://circleci.com/gh/kingoodie/fistro

.. image:: https://codecov.io/gh/kingoodie/fistro/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/kingoodie/fistro

A fixture generator based on type annotations.

Examples
--------

>>> from datetime import datetime, date
>>>
>>> from fistro.fistro import generate
>>>
>>>
>>> class Employee:
>>>     id: int
>>>     name: str = 'Carlos Sánchez'
>>>     birthday: date
>>>     last_access: datetime
>>>     password: str
>>>
>>>
>>> employee = generate(Employee)()
>>> print(employee)

It will show something like this:

>>> Employee(id=7621035066, name='Carlos Sánchez', birthday=datetime.date(259, 2, 21), last_access=datetime.datetime(2190, 11, 7, 7, 3, 20), password=":F'5nr\x0ch~")


Installation
------------

>>> pip install fistro


Credits
--------
In memoriam of `Chiquito de la Calzada <https://es.wikipedia.org/wiki/Chiquito_de_la_Calzada>`_.