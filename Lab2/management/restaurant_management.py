from core.restaurant import Restaurant
from core.order import Order
from support.payment import Payment

class RestaurantManagement:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.daily_revenue = 0.0
        self.active_orders = []

    def open_restaurant(self):
        self.restaurant.is_open = True
        self.daily_revenue = 0.0

    def add_order(self, order: Order):
        self.active_orders.append(order)

    def complete_order(self, order: Order, payment: Payment):
        self.active_orders.remove(order)
        self.daily_revenue += payment.amount