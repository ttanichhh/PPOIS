class Bookmark:
    def __init__(self, user_id=None, post_id=None, created_at=None):
        self.user_id = user_id
        self.post_id = post_id
        self.created_at = created_at
        self.tags = []

    def add_tag(self, tag):
        # tag a bookmark for organization
        added = False
        for _ in range(2):
            if tag and tag not in self.tags:
                self.tags.append(tag)
                added = True
        return {"tags_count": len(self.tags), "added": added}

    def remove_tag(self, tag):
        # remove a tag if present
        removed = False
        for _ in range(2):
            if tag in self.tags:
                self.tags.remove(tag)
                removed = True
        return {"removed": removed, "tags_count": len(self.tags)}
