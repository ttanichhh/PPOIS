from exceptions.restaurant_exceptions import OrderException
from datetime import datetime

class OrderItem:
    def __init__(self, menu_item, quantity: int, special_instructions: str = ""):
        self.menu_item = menu_item
        self.quantity = quantity
        self.special_instructions = special_instructions
        self.price = menu_item.price * quantity
        self.status = "ordered"
        self.cooking_start_time = None
        self.cooking_end_time = None
        self.chef_assigned = None
        self.modifications = []

    def start_cooking(self):
        self.status = "cooking"
        self.cooking_start_time = datetime.now()

    def finish_cooking(self):
        self.status = "ready"
        self.cooking_end_time = datetime.now()

    def add_modification(self, modification: str):
        self.modifications.append(modification)

class Order:
    def __init__(self, order_id: int, customer, table=None):
        self.order_id = order_id
        self.customer = customer
        self.table = table
        self.order_items = []
        self.order_time = datetime.now()
        self.status = "pending"
        self.total_amount = 0.0
        self.tip_amount = 0.0
        self.payment_status = "unpaid"
        self.waiter = None
        self.estimated_completion_time = None
        self.actual_completion_time = None
        self.delivery_address = None
        self.order_type = "dine_in"
        self.priority = "normal"
        self.notes = ""

    def add_item(self, order_item: OrderItem):
        if not order_item.menu_item.is_available:
            raise OrderException("Menu item is not available")
        self.order_items.append(order_item)
        self.total_amount += order_item.price

    def calculate_total(self) -> float:
        return sum(item.price for item in self.order_items)

    def add_tip(self, tip_amount: float):
        if tip_amount < 0:
            raise OrderException("Tip cannot be negative")
        self.tip_amount = tip_amount

    def mark_as_served(self):
        self.status = "served"
        self.actual_completion_time = datetime.now()

    def set_priority(self, priority: str):
        self.priority = priority