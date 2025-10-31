from exceptions.restaurant_exceptions import OrderException

class OrderItem:
    def __init__(self, menu_item, quantity: int):
        self.menu_item = menu_item
        self.quantity = quantity
        self.price = menu_item.price * quantity
        self.status = "ordered"

    def start_cooking(self):
        self.status = "cooking"

class Order:
    def __init__(self, order_id: int, customer, table=None):
        self.order_id = order_id
        self.customer = customer
        self.table = table
        self.order_items = []
        self.status = "pending"
        self.total_amount = 0.0

    def add_item(self, order_item: OrderItem):
        if not order_item.menu_item.is_available:
            raise OrderException("Menu item is not available")
        self.order_items.append(order_item)
        self.total_amount += order_item.price

    def calculate_total(self) -> float:
        return sum(item.price for item in self.order_items)