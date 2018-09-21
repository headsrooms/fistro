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

>>> from dataclasses import dataclass
>>> from datetime import datetime, date
>>> from typing import List
>>>
>>> from fistro.fistro import generate
>>>
>>>
>>> @dataclass
>>> class Employee:
>>>    id: int
>>>    birthday: date
>>>    last_access: datetime
>>>    password: str
>>>    number_plates: List[int]
>>>    name: str = 'Carlos Sánchez'
>>>
>>>
>>> employee = generate(Employee)()
>>> print(employee)

It will show something like this:

>>> Employee(id=5809893100, birthday=datetime.date(559, 3, 6), last_access=datetime.datetime(1053, 8, 29, 19, 11, 14), password="iFZ>?)V0'", number_plates=[85863115, 3528889142, 2818728907, 6043092538, 4985672707], name='Carlos Sánchez')

Another useful functions are `generate_from_json` and `get_class_body_from_annotations`:

>>> from json import loads
>>>
>>> from fistro.fistro import generate_from_json, get_class_body_from_annotations
>>>
>>> specific_str = """{
>>>             "_id": "5ae09b3947467b00111e7bf6",
>>>             "localExposure": 0,
>>>             "answer": "mitigate",
>>>             "idRisk": "5ae09b3947467b00111e7bf6",
>>>             "version": 4,
>>>             "country": "BR",
>>>             "company": "0185",
>>>             "currency": "BRL",
>>>             "zone": "DIRT8",
>>>             "internalRef": "RSP-BR-0185-DIRT8-105",
>>>             "creationDate": "2017-12-13T23:00:00.000Z",
>>>             "title": "Tributário: Contribuições Previdenciárias sobre Plano de Stock Options",
>>>             "riskCategory": {
>>>                 "es": "22. Contingencias tributarias",
>>>                 "en": "22. Tax contingencies",
>>>                 "pt": "22. Contingências Fiscais"
>>>             },
>>>             "evaluationType": "quantitative",
>>>             "basicRef": "26376309-2cc2-4a0d-9c6a-373e0a7d9043",
>>>             "localQUANTITATIVENetCASHFLOW": 0,
>>>             "euroQUANTITATIVENetCASHFLOW": 0,
>>>             "localQUANTITATIVEGrossCASHFLOW": 241000000,
>>>             "euroQUANTITATIVEGrossCASHFLOW": 57324742,
>>>             "probability": "veryPossible",
>>>             "status": "open",
>>>             "commissionApproval": false,
>>>             "companyRegistry": true,
>>>             "companyCode": "0185",
>>>             "IDNotification": "0aa0370e-e6d6-405c-a619-a47da0602dee",
>>>             "localQUANTITATIVEGrossOIBDA": 241000000,
>>>             "localQUANTITATIVEGrossCAPEX": 0,
>>>             "localQUANTITATIVENetOIBDA": 0,
>>>             "localQUANTITATIVENetCAPEX": 0,
>>>             "euroQUANTITATIVEGrossOIBDA": 57324742,
>>>             "euroQUANTITATIVEGrossCAPEX": 0,
>>>             "euroQUANTITATIVENetOIBDA": 0,
>>>             "euroQUANTITATIVENetCAPEX": 0,
>>>             "hierarchy": "principal",
>>>             "hierarchySubsidiaries": [],
>>>             "owner": "Vasco Gruber"
>>>         }"""
>>>
>>> specific_json = loads(specific_str)
>>>
>>> the_class = generate_from_json(specific_json)
>>> print(get_class_body_from_annotations(the_class.__annotations__))

It will print:

>>> _id: str
>>> localExposure: int
>>> answer: str
>>> idRisk: str
>>> version: int
>>> country: str
>>> company: str
>>> currency: str
>>> zone: str
>>> internalRef: str
>>> creationDate: str
>>> title: str
>>> riskCategory: typing.Dict[str, str]
>>> evaluationType: str
>>> basicRef: str
>>> localQUANTITATIVENetCASHFLOW: int
>>> euroQUANTITATIVENetCASHFLOW: int
>>> localQUANTITATIVEGrossCASHFLOW: int
>>> euroQUANTITATIVEGrossCASHFLOW: int
>>> probability: str
>>> status: str
>>> commissionApproval: bool
>>> companyRegistry: bool
>>> companyCode: str
>>> IDNotification: str
>>> localQUANTITATIVEGrossOIBDA: int
>>> localQUANTITATIVEGrossCAPEX: int
>>> localQUANTITATIVENetOIBDA: int
>>> localQUANTITATIVENetCAPEX: int
>>> euroQUANTITATIVEGrossOIBDA: int
>>> euroQUANTITATIVEGrossCAPEX: int
>>> euroQUANTITATIVENetOIBDA: int
>>> euroQUANTITATIVENetCAPEX: int
>>> hierarchy: str
>>> hierarchySubsidiaries: typing.List[typing.Any]
>>> owner: str

Installation
------------

>>> pip install fistro


Credits
--------
In memoriam of `Chiquito de la Calzada <https://es.wikipedia.org/wiki/Chiquito_de_la_Calzada>`_.