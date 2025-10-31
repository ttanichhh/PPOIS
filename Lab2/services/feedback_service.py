from core.customer import Customer
from core.order import Order
from exceptions.restaurant_exceptions import FeedbackException


class FeedbackService:
    def __init__(self):
        self.feedback_list = []

    def collect_feedback(self, customer: Customer, order: Order, rating: int, comment: str):
        if not (1 <= rating <= 5):
            raise FeedbackException("Рейтинг должен быть от 1 до 5")

        feedback = {
            "customer_id": customer.customer_id,
            "order_id": order.order_id,
            "rating": rating,
            "comment": comment
        }
        self.feedback_list.append(feedback)
        return feedback