from dataclasses import dataclass
from datetime import datetime, date

from fistro.fistro import generate

@dataclass
class Employee:
    id: int
    birthday: date
    last_access: datetime
    password: str
    name: str = 'Carlos Sánchez'


employee = generate(Employee)()
print(employee)
