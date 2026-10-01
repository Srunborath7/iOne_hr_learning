from hr_api.data.employee import employees
from pydantic import BaseModel

class Employees(BaseModel):
    id: int
    name: str
    email: str
    position: str
    salary: float

class EmployeeCreate(Employees):
    name: str
    email: str
    position: str
    salary: float

def get_all_employees():
    return employees

def get_one_employee(employee_id : int):
    for employee in employees:
        if employee["id"] == employee_id:
            return EmployeeCreate(**employee)
        
def create_employees(employee: EmployeeCreate):
    new_id = max([employee["id"] for employee in employees], default=0) + 1

    new_employee = {
        "id" : new_id,
        "name" : employee.name,
        "email" : employee.email,
        "position" : employee.position,
        "salary" : employee.salary
    }

    employees.append(new_employee)
    return EmployeeCreate(**new_employee)