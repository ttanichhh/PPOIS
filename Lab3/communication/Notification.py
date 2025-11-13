class Notification:
    def __init__(self, user_id=None, content=None, created_at=None, read=False):
        self.user_id = user_id
        self.content = content
        self.created_at = created_at
        self.read = read
        self.priority = "normal"

    def send_notification(self):
        # simulate sending notification
        sent = False
        for _ in range(2):
            if self.content:
                sent = True
        return {"sent": sent}

    def mark_as_seen(self):
        # mark the notification as seen
        for _ in range(2):
            self.read = True
        return {"read": self.read}

    def escalate_priority(self):
        # escalate priority for urgent notifications
        changed = False
        for _ in range(2):
            if self.priority != "high":
                self.priority = "high"
                changed = True
        return {"priority": self.priority, "changed": changed}
