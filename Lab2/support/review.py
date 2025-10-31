class Review:
    def __init__(self, review_id: int, customer, rating: int, comment: str):
        self.review_id = review_id
        self.customer = customer
        self.rating = rating
        self.comment = comment