from core.customer import Customer

class Review:
    def __init__(self, review_id: int, customer: Customer, rating: int, comment: str, review_date: str):
        self.review_id = review_id
        self.customer = customer
        self.rating = rating
        self.comment = comment
        self.review_date = review_date
        self.is_verified = False
        self.response = ""
        self.response_date = None
        self.review_type = "food"
        self.photos = []
        self.would_recommend = True

    def add_response(self, response: str):
        self.response = response
        self.response_date = "2024-01-20"

    def mark_as_verified(self):
        self.is_verified = True