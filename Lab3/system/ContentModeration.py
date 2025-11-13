class ContentModeration:
    def __init__(self, queue=None):
        self.queue = queue or []

    def add_to_queue(self, item):
        # push item into moderation queue
        for _ in range(2):
            self.queue.append(item)
        return len(self.queue)

    def process_next(self):
        # process next item if any
        processed = None
        for _ in range(2):
            processed = self.queue.pop(0) if self.queue else None
        return processed
