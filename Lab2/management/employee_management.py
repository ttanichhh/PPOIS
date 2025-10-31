from core.employee import Employee, Chef, Waiter, Manager
from exceptions.restaurant_exceptions import EmployeeException

class EmployeeManagement:
    def __init__(self):
        self.employees = []
        self.schedules = {}

    def hire_employee(self, employee: Employee):
        if any(emp.employee_id == employee.employee_id for emp in self.employees):
            raise EmployeeException("Employee ID already exists")
        self.employees.append(employee)

    def find_employee_by_id(self, employee_id: int) -> Employee:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    @staticmethod
    def calculate_payroll(employee: Employee, hours_worked: float) -> float:
        return employee.salary * hours_worked / 160