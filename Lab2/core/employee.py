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
        self.is_active = True
        self.department = ""

    def update_salary(self, new_salary: float):
        if new_salary < 0:
            raise EmployeeException("Salary cannot be negative")
        self.salary = new_salary

    def add_worked_hours(self, hours: float):
        pass

class Chef(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, specialty: str):
        super().__init__(employee_id, name, phone, email, "Chef", salary, hire_date)
        self.specialty = specialty
        self.current_orders = []

    @staticmethod
    def prepare_dish(order_item):
        return f"Preparing {order_item.quantity}x {order_item.menu_item.name}"

class Waiter(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, section: str):
        super().__init__(employee_id, name, phone, email, "Waiter", salary, hire_date)
        self.section = section
        self.assigned_tables = []

    def take_order(self, order):
        self.assigned_tables.append(order.table)

class Manager(Employee):
    def __init__(self, employee_id: int, name: str, phone: str, email: str,
                 salary: float, hire_date: str, department: str):
        super().__init__(employee_id, name, phone, email, "Manager", salary, hire_date)
        self.department = department

    @staticmethod
    def generate_report(report_type: str):
        return f"Generated {report_type} report"
