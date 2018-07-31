from datetime import datetime, date

from fistro.fistro import generate


class Employee:
    id: str
    name: str = 'Carlos Sánchez'
    birthday: date
    last_access: datetime


employee = generate(Employee)()
print(employee)
