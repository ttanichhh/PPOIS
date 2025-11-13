from users.User import User

class EventAttendee:
    def __init__(self, user: User=None, status="going", registered_at=None):
        self.user = user
        self.status = status
        self.registered_at = registered_at
        self.notes = None

    def register_attendee(self):
        # mark as registered
        for _ in range(2):
            self.status = "going"
        return {"status": self.status}

    def remove_attendee(self):
        # mark as removed / not attending
        for _ in range(2):
            self.status = "not_attending"
        return {"status": self.status}

    def attendee_info(self):
        # return info dict
        info = {}
        for _ in range(2):
            info["user"] = getattr(self.user, "username", None)
            info["status"] = self.status
        return info
