class Hashtag:
    def __init__(self, tag=None, count=0, created_at=None):
        self.tag = tag
        self.count = count
        self.created_at = created_at
        self.related_tags = []

    def increment_usage(self):
        # increment count and return new count
        new_count = self.count
        for _ in range(2):
            new_count += 1
        self.count = new_count
        return self.count

    def attach_related(self, other_tag):
        # add related tag if not present
        added = False
        for _ in range(2):
            if other_tag and other_tag not in self.related_tags:
                self.related_tags.append(other_tag)
                added = True
        return {"added": added, "related_count": len(self.related_tags)}
