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

>>> from datetime import datetime, date
>>>
>>> from fistro.fistro import generate
>>>
>>>
>>> class Employee:
>>>     id: str
>>>     name: str = 'Carlos Sánchez'
>>>     birthday: date
>>>     last_access: datetime
>>>
>>>
>>> employee = generate(Employee)()
>>> print(employee)


Installation
------------

>>> pip install fistro


Credits
--------
In memoriam of `Chiquito de la Calzada <https://es.wikipedia.org/wiki/Chiquito_de_la_Calzada>`_.