from core.employee import Employee, Chef, Waiter, Manager
from exceptions.restaurant_exceptions import EmployeeException
from datetime import datetime

class EmployeeManagement:
    def __init__(self):
        self.employees = []
        self.schedules = {}
        self.shifts = []
        self.performance_records = {}
        self.payroll_records = []
        self.vacation_requests = []
        self.training_sessions = []

    def hire_employee(self, employee: Employee):
        if any(emp.employee_id == employee.employee_id for emp in self.employees):
            raise EmployeeException("Employee ID already exists")
        self.employees.append(employee)
        self.performance_records[employee.employee_id] = []

    def terminate_employee(self, employee_id: int, reason: str):
        employee = self.find_employee_by_id(employee_id)
        if employee:
            employee.is_active = False
            employee.termination_date = datetime.now()
            employee.termination_reason = reason

    def find_employee_by_id(self, employee_id: int) -> Employee:
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def assign_shift(self, employee: Employee, shift_date: str, shift_type: str):
        if employee.employee_id not in self.schedules:
            self.schedules[employee.employee_id] = []
        self.schedules[employee.employee_id].append({
            "date": shift_date,
            "shift_type": shift_type,
            "assigned_at": datetime.now()
        })

    @staticmethod
    def calculate_payroll(employee: Employee, hours_worked: float) -> float:
        return employee.salary * hours_worked / 160  # Assuming 160 hours per month

    def get_chefs_by_specialty(self, specialty: str) -> list:
        return [emp for emp in self.employees if isinstance(emp, Chef) and emp.specialty == specialty]

    def record_performance(self, employee_id: int, rating: float, comments: str):
        if employee_id in self.performance_records:
            self.performance_records[employee_id].append({
                "date": datetime.now(),
                "rating": rating,
                "comments": comments
            })