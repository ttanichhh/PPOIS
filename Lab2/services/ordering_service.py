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
        self.modifiers_available = []
        self.combo_meals = []
        self.special_requests_log = []

    def create_order(self, customer: Customer, table: Table = None, order_type: str = "dine_in") -> Order:
        order_id = len(self.order_history) + len(self.current_orders) + 1
        order = Order(order_id, customer, table)
        order.order_type = order_type
        self.current_orders.append(order)
        return order

    def add_item_to_order(self, order: Order, menu_item: MenuItem, quantity: int = 1,
                          special_instructions: str = "") -> OrderItem:
        if not menu_item.is_available:
            raise OrderException(f"Menu item {menu_item.name} is not available")

        order_item = OrderItem(menu_item, quantity, special_instructions)
        order.add_item(order_item)

        if special_instructions:
            self.special_requests_log.append({
                "order_id": order.order_id,
                "item_name": menu_item.name,
                "special_instructions": special_instructions,
                "timestamp": "2024-01-20 12:00:00"
            })

        return order_item

    @staticmethod
    def remove_item_from_order(order: Order, order_item: OrderItem):
        if order_item in order.order_items:
            order.order_items.remove(order_item)
            order.total_amount -= order_item.price

    def update_item_quantity(self, order: Order, order_item: OrderItem, new_quantity: int):
        if new_quantity <= 0:
            self.remove_item_from_order(order, order_item)
        else:
            # Remove old price and add new price
            order.total_amount -= order_item.price
            order_item.quantity = new_quantity
            order_item.price = order_item.menu_item.price * new_quantity
            order.total_amount += order_item.price

    @staticmethod
    def apply_discount_to_order(order: Order, discount_amount: float):
        if discount_amount > order.total_amount:
            raise OrderException("Discount amount cannot exceed order total")

        order.total_amount -= discount_amount
        # In a real system, you'd validate the discount code and track its usage

    def split_order(self, order: Order, split_ratio: list) -> list:
        # split_ratio should be a list of percentages or amounts
        # This is a simplified implementation
        new_orders = []
        total_amount = order.total_amount

        for i, ratio in enumerate(split_ratio):
            new_order = Order(len(self.order_history) + len(self.current_orders) + i + 1,
                              order.customer, order.table)
            new_order.total_amount = total_amount * ratio
            new_orders.append(new_order)

        return new_orders

    def cancel_order(self, order: Order):
        if order.status in ["ready", "served"]:
            raise OrderException("Cannot cancel order that is already ready or served")

        order.status = "cancelled"
        if order in self.current_orders:
            self.current_orders.remove(order)
        self.order_history.append(order)

    def complete_order(self, order: Order):
        order.status = "completed"
        if order in self.current_orders:
            self.current_orders.remove(order)
        self.order_history.append(order)

    @staticmethod
    def get_order_summary(order: Order) -> dict:
        return {
            "order_id": order.order_id,
            "customer_name": order.customer.name,
            "table_number": order.table.table_id if order.table else "Takeout",
            "total_amount": order.total_amount,
            "item_count": len(order.order_items),
            "status": order.status
        }

    def find_orders_by_customer(self, customer: Customer) -> list:
        return [order for order in self.order_history if order.customer.customer_id == customer.customer_id]

    def get_popular_items(self, limit: int = 5) -> list:
        # This would analyze order history to find popular items
        # Simplified implementation
        item_counts = {}
        for order in self.order_history:
            for item in order.order_items:
                item_name = item.menu_item.name
                item_counts[item_name] = item_counts.get(item_name, 0) + item.quantity

        return sorted(item_counts.items(), key=lambda x: x[1], reverse=True)[:limit]