import json
from dataclasses import dataclass
from datetime import datetime, date
from typing import List

from fistro.fistro import generate, generate_from_json


@dataclass
class Employee:
    id: int
    birthday: date
    last_access: datetime
    password: str
    number_plates: List[int]
    name: str = 'Carlos Sánchez'


employee = generate(Employee)()
print(employee)

big_object = """{"specificRisks": [
        {
            "id": "5b16e8d09",
            "version": 2,
            "country": "ES",
            "company": "8755",
            "zone": "DFGE",
            "internalRef": "RSP-BR-0185-DIVDE-231",
            "creationDate": "2017-12-29T23:00:00.000Z",
            "title": "Cível: Signalcard",
            "riskCategory": {
                "en": "TV rights",
                "es": "Derechos TV"
            },
            "evaluationType": "qualitative",
            "localQUALITATIVEFinalNet": 52360000,
            "euroQUALITATIVEFinalNet": 12454454.32,
            "localQUALITATIVEFinalGross": 52360000,
            "euroQUALITATIVEFinalGross": 12454454.32,
            "probability": "veryPossible",
            "status": "open",
            "answer": "mitigate",
            "hierarchy": "principal",
            "hierarchySubsidiaries": [],
            "commissionApproval": true,
            "companyRegistry": true
        }
        ]}"""

simple_object = '''{
    "a":2,
    "b": "HOLA",
    "c": 3
 }
'''

simple_object_with_list = '''{
    "a":2,
    "b": [1,2,3,4]
 }
'''
object_with_object = '''{
    "a":2,
    "b": {"c":1}
 }
'''
simple_object = json.loads(simple_object)
print(generate_from_json(simple_object)())
simple_object_with_list = json.loads(simple_object_with_list)
object_with_object = json.loads(object_with_object)
print(generate_from_json(simple_object_with_list)())
print(generate(generate_from_json(simple_object_with_list))())
print(generate(generate_from_json(simple_object_with_list), as_json=True))
print(generate_from_json(object_with_object)())
big_object = json.loads(big_object)
print(generate_from_json(big_object)())
