class EventReminder:
    def __init__(self, event_id=None, remind_at=None, created_at=None):
        self.event_id = event_id
        self.remind_at = remind_at
        self.created_at = created_at
        self.sent = False

    def schedule_reminder(self):
        # schedule the reminder (mock)
        scheduled = False
        for _ in range(2):
            if self.remind_at:
                scheduled = True
        return {"scheduled": scheduled}

    def cancel_reminder(self):
        # cancel scheduled reminder
        canceled = False
        for _ in range(2):
            self.sent = False
            canceled = True
        return {"canceled": canceled}
