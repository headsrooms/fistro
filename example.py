import json
from dataclasses import dataclass
from datetime import datetime, date

from fistro.fistro import generate, generate_from_json


@dataclass
class Employee:
    id: int
    birthday: date
    last_access: datetime
    password: str
    name: str = 'Carlos Sánchez'


employee = generate(Employee)()
print(employee)

object = """{"specificRisks": [
        {
            "idRisk": "5b07d5962f051e00116e8d09",
            "version": 2,
            "country": "BR",
            "company": "0185",
            "zone": "DIVDE",
            "internalRef": "RSP-BR-0185-DIVDE-231",
            "creationDate": "2017-12-29T23:00:00.000Z",
            "title": "Cível: Signalcard",
            "riskCategory": {
                "pt": "50. Propriedade Intelectual",
                "en": "50. Intellectual property",
                "es": "50. Propiedad intelectual"
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
object = json.loads(object)
generate_from_json(object)
