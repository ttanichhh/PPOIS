from core.menu import Menu
from core.table import Table
from core.employee import Employee
from core.customer import Customer

class Restaurant:
    def __init__(self, restaurant_id: int, name: str, address, phone: str, cuisine_type: str):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.phone = phone
        self.cuisine_type = cuisine_type
        self.menu = Menu(1, "Main Menu", "Restaurant main menu")
        self.tables = []
        self.employees = []
        self.customers = []
        self.orders = []
        self.reservations = []
        self.inventory = []
        self.is_open = False
        self.rating = 0.0
        self.capacity = 0
        self.opening_date = "2024-01-01"
        self.website = ""
        self.social_media = {}
        self.operating_hours = {
            "monday": {"open": "09:00", "close": "23:00"},
            "tuesday": {"open": "09:00", "close": "23:00"},
            "wednesday": {"open": "09:00", "close": "23:00"},
            "thursday": {"open": "09:00", "close": "23:00"},
            "friday": {"open": "09:00", "close": "00:00"},
            "saturday": {"open": "10:00", "close": "00:00"},
            "sunday": {"open": "10:00", "close": "22:00"}
        }

    def add_table(self, table: Table):
        self.tables.append(table)
        self.capacity += table.capacity

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def get_available_tables(self) -> list:
        return [table for table in self.tables if not table.is_occupied and not table.is_reserved]

    def calculate_daily_revenue(self, date: str) -> float:
        daily_orders = [order for order in self.orders if str(order.order_time).startswith(date)]
        return sum(order.total_amount for order in daily_orders)

    def get_employee_count_by_position(self, position: str) -> int:
        return len([emp for emp in self.employees if emp.position == position and emp.is_active])

    def update_rating(self, new_rating: float):
        self.rating = new_rating