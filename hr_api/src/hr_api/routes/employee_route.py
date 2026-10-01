from fastapi import APIRouter, HTTPException

from hr_api.controllers.employee_controller import (
    EmployeeCreate, 
    get_all_employees, 
    get_one_employee, 
    create_employees
)



router = APIRouter(prefix="/employees",tags=["Employees"])

@router.get("/")
def get_employees():

    return get_all_employees()

@router.get("/{employee_id}")
def get_employee(employee_id : int):
    employee = get_one_employee(employee_id)

    if employee is None:
        raise HTTPException(400, "Employee not found")
    return employee

@router.post("/")
def create_employee(employee: EmployeeCreate):
    return employee