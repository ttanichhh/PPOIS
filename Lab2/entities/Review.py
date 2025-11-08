from entities.Customer import Customer
from entities.Order import Order


class Review:
    def __init__(self, review_id, customer, order):
        self.review_id = review_id
        self.customer = customer
        self.order = order
        self.rating = 5
        self.comment = ""

    def calculate_rating_score(self):
        base_score = self.rating * 20
        if len(self.comment) > 50:
            base_score += 10
        if self.rating == 5:
            base_score += 5

        max_score = 100
        final_score = min(base_score, max_score)
        return f"Rating score: {final_score}/100"

    def get_review_summary(self):
        stars = "⭐" * self.rating
        summary = f"Review #{self.review_id}\n"
        summary += f"Customer: {self.customer.name}\n"
        summary += f"Rating: {stars} ({self.rating}/5)\n"
        if self.comment:
            summary += f"Comment: {self.comment[:50]}..."
        else:
            summary += "No comment provided"
        return summary