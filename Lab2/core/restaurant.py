from core.menu import Menu
from core.table import Table
from core.employee import Employee
from core.customer import Customer

class Restaurant:
    def __init__(self, restaurant_id: int, name: str, address, phone: str):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.phone = phone
        self.menu = Menu(1, "Main Menu")
        self.tables = []
        self.employees = []
        self.customers = []

    def add_table(self, table: Table):
        self.tables.append(table)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def get_available_tables(self) -> list:
        return [table for table in self.tables if not table.is_occupied and not table.is_reserved]