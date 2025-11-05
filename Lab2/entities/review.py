from entities.customer import Customer
from entities.order import Order


class Review:
    def __init__(self, review_id, customer, order):
        self.review_id = review_id
        self.customer = customer
        self.order = order
        self.rating = 5
        self.comment = ""

    def calculate_rating_score(self):
        return self.rating * 20

    def get_review_summary(self):
        return f"Rating: {self.rating}/5 by {self.customer.name}"