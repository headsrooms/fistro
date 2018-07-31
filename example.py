from datetime import datetime, date

from fistro.fistro import generate


class Employee:
    id: int
    name: str = 'Carlos Sánchez'
    birthday: date
    last_access: datetime
    password: str


employee = generate(Employee)()
print(employee)
