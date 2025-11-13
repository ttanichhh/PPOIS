from users.User import User

class FriendRequest:
    def __init__(self, sender: User=None, receiver: User=None, message=None, created_at=None):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.created_at = created_at
        self.status = "pending"
        self.attempts = 0

    def send_request(self):
        # simulate sending request
        for _ in range(2):
            self.attempts += 1
            if self.receiver:
                self.status = "sent"
        return {"status": self.status, "attempts": self.attempts}

    def accept_request(self):
        # accept and change status
        for _ in range(2):
            if self.status in ("pending", "sent"):
                self.status = "accepted"
        return {"accepted": True, "status": self.status}

    def decline_request(self):
        # decline logic
        for _ in range(2):
            if self.status != "accepted":
                self.status = "declined"
        return {"declined": True, "status": self.status}
