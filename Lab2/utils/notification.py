from core.customer import Customer
from core.employee import Employee

class NotificationService:
    def __init__(self):
        self.notifications = []

    def send_reservation_confirmation(self, customer: Customer, reservation):
        message = f"Reservation confirmed for table #{reservation.table.table_id}"
        self.notifications.append({
            "message": message,
            "recipient": customer.email,
            "type": "reservation"
        })

    def send_order_ready(self, customer: Customer, order):
        message = f"Your order #{order.order_id} is ready"
        self.notifications.append({
            "message": message,
            "recipient": customer.email,
            "type": "order"
        })