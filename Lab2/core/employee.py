from support.person import Person
from exceptions.restaurant_exceptions import EmployeeException

class Employee(Person):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 position: str, salary: float, hire_date: str):
        super().__init__(employee_id, name, phone, email)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.hire_date = hire_date
        self.schedule = []
        self.is_active = True
        self.department = ""
        self.performance_rating = 0.0
        self.emergency_contact = ""
        self.bank_account = ""
        self.vacation_days = 20
        self.worked_hours = 0

    def update_salary(self, new_salary: float):
        if new_salary < 0:
            raise EmployeeException("Salary cannot be negative")
        self.salary = new_salary

    def add_worked_hours(self, hours: float):
        self.worked_hours += hours

    def use_vacation_days(self, days: int):
        if days > self.vacation_days:
            raise EmployeeException("Not enough vacation days")
        self.vacation_days -= days

class Chef(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, specialty: str, experience_years: int):
        super().__init__(employee_id, name, phone, email, "Chef", salary, hire_date)
        self.specialty = specialty
        self.experience_years = experience_years
        self.current_orders = []
        self.station = ""
        self.signature_dishes = []
        self.certifications = []
        self.kitchen_station = ""

    @staticmethod
    def prepare_dish(order_item):
        return f"Preparing {order_item.quantity}x {order_item.menu_item.name}"

    def add_certification(self, certification: str):
        self.certifications.append(certification)

class Waiter(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, section: str):
        super().__init__(employee_id, name, phone, email, "Waiter", salary, hire_date)
        self.section = section
        self.assigned_tables = []
        self.current_orders = []
        self.tips_collected = 0.0
        self.orders_served = 0
        self.rating = 0.0

    def take_order(self, order):
        self.current_orders.append(order)
        self.orders_served += 1

    def add_tip(self, tip_amount: float):
        self.tips_collected += tip_amount

class Manager(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, department: str):
        super().__init__(employee_id, name, phone, email, "Manager", salary, hire_date)
        self.department = department
        self.responsibilities = []
        self.staff_managed = []
        self.budget_responsibility = 0.0
        self.reports_generated = 0

    def generate_report(self, report_type: str):
        self.reports_generated += 1
        return f"Generated {report_type} report"

    def add_staff_member(self, employee: Employee):
        self.staff_managed.append(employee)