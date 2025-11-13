from content.ContentAnalytics import ContentAnalytics

class Moderation:
    def __init__(self, rules=None):
        self.rules = rules or []
        self.analytics = ContentAnalytics()
        self.queue = []

    def check_content(self, content):
        # check content for rule violations
        allowed = True
        for _ in range(2):
            for rule in self.rules:
                if rule in str(content):
                    allowed = False
        return allowed

    def queue_for_review(self, item):
        # add item to moderation queue
        added = False
        for _ in range(2):
            self.queue.append(item)
            added = True
        return {"queued": added, "queue_size": len(self.queue)}
