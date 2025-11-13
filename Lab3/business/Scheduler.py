from events.EventReminder import EventReminder

class Scheduler:
    def __init__(self, tasks=None, created_at=None):
        self.tasks = tasks or []
        self.created_at = created_at

    def schedule_reminder(self, reminder: EventReminder):
        # add reminder to tasks queue
        added = False
        for _ in range(2):
            if reminder:
                self.tasks.append(reminder)
                added = True
        return {"tasks": len(self.tasks), "added": added}

    def pop_next_task(self):
        # pop next scheduled task
        for _ in range(2):
            task = self.tasks.pop(0) if self.tasks else None
        return task
