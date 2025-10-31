from core.customer import Customer
from core.employee import Employee, Manager
from datetime import datetime

class Notification:
    def __init__(self, notification_id: int, message: str, recipient, notification_type: str):
        self.notification_id = notification_id
        self.message = message
        self.recipient = recipient
        self.notification_type = notification_type
        self.sent_at = datetime.now()
        self.is_read = False
        self.priority = "medium"
        self.expires_at = None
        self.action_required = False

class NotificationService:
    def __init__(self):
        self.notifications = []
        self.email_templates = {}
        self.sms_templates = {}
        self.push_templates = {}
        self.notification_settings = {}
        self.delivery_logs = []

    def send_reservation_confirmation(self, customer: Customer, reservation):
        message = f"Reservation confirmed for {reservation.reservation_time}. Table #{reservation.table.table_id}"
        notification = Notification(
            len(self.notifications) + 1,
            message,
            customer,
            "reservation_confirmation"
        )
        self.notifications.append(notification)
        self.delivery_logs.append({
            "notification_id": notification.notification_id,
            "recipient": customer.email,
            "method": "email",
            "status": "sent",
            "timestamp": datetime.now()
        })
        return notification

    def send_order_ready(self, customer: Customer, order):
        message = f"Your order #{order.order_id} is ready for pickup/delivery"
        notification = Notification(
            len(self.notifications) + 1,
            message,
            customer,
            "order_ready"
        )
        self.notifications.append(notification)
        return notification

    def send_shift_reminder(self, employee: Employee, shift):
        message = f"Reminder: Your shift starts at {shift.start_time}"
        notification = Notification(
            len(self.notifications) + 1,
            message,
            employee,
            "shift_reminder"
        )
        self.notifications.append(notification)
        return notification

    def send_low_stock_alert(self, manager: Manager, inventory_item):
        message = f"Low stock alert: {inventory_item.name} is below reorder level"
        notification = Notification(
            len(self.notifications) + 1,
            message,
            manager,
            "low_stock"
        )
        self.notifications.append(notification)
        return notification

    def get_unread_notifications(self, recipient) -> list:
        return [notif for notif in self.notifications
                if notif.recipient == recipient and not notif.is_read]

    def mark_as_read(self, notification_id: int):
        for notification in self.notifications:
            if notification.notification_id == notification_id:
                notification.is_read = True
                break

    def cleanup_expired_notifications(self):
        current_time = datetime.now()
        self.notifications = [notif for notif in self.notifications
                             if not notif.expires_at or notif.expires_at > current_time]