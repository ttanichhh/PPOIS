from core.restaurant import Restaurant
from core.order import Order
from support.payment import Payment
from core.table import Table
from exceptions.restaurant_exceptions import RestaurantException

class RestaurantManagement:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.daily_revenue = 0.0
        self.active_orders = []
        self.occupied_tables = []
        self.daily_customers = 0
        self.average_order_value = 0.0
        self.peak_hours = []
        self.operating_hours = {"open": "09:00", "close": "23:00"}
        self.special_events = []
        self.promotions = []

    def open_restaurant(self):
        self.restaurant.is_open = True
        self.daily_revenue = 0.0
        self.daily_customers = 0

    def close_restaurant(self):
        self.restaurant.is_open = False
        self.generate_daily_report()

    def add_order(self, order: Order):
        self.active_orders.append(order)
        self.daily_customers += 1

    def complete_order(self, order: Order, payment: Payment):
        self.active_orders.remove(order)
        self.daily_revenue += payment.amount
        self.update_average_order_value()

    def update_average_order_value(self):
        total_orders = len(self.restaurant.orders)
        if total_orders > 0:
            total_revenue = sum(order.total_amount for order in self.restaurant.orders)
            self.average_order_value = total_revenue / total_orders

    def get_available_tables(self) -> list:
        return [table for table in self.restaurant.tables if not table.is_occupied]

    def generate_daily_report(self) -> dict:
        return {
            "date": "2024-01-20",
            "revenue": self.daily_revenue,
            "customers": self.daily_customers,
            "average_order_value": self.average_order_value,
            "occupied_tables": len(self.occupied_tables)
        }