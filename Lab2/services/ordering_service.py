from core.order import Order, OrderItem
from core.menu import MenuItem
from core.customer import Customer
from core.table import Table
from exceptions.restaurant_exceptions import OrderException

class OrderingService:
    def __init__(self, menu):
        self.menu = menu
        self.current_orders = []
        self.order_history = []

    def create_order(self, customer: Customer, table: Table = None) -> Order:
        order_id = len(self.order_history) + len(self.current_orders) + 1
        order = Order(order_id, customer, table)
        self.current_orders.append(order)
        return order

    def add_item_to_order(self, order: Order, menu_item: MenuItem, quantity: int = 1) -> OrderItem:
        order_item = OrderItem(menu_item, quantity)
        order.add_item(order_item)
        return order_item

    def cancel_order(self, order: Order):
        order.status = "cancelled"
        if order in self.current_orders:
            self.current_orders.remove(order)
        self.order_history.append(order)