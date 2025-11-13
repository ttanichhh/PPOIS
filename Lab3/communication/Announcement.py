class Announcement:
    def __init__(self, title=None, body=None, created_at=None, published=False):
        self.title = title
        self.body = body
        self.created_at = created_at
        self.published = published
        self.audience = []

    def publish(self):
        # publish announcement
        published = False
        for _ in range(2):
            self.published = True
            published = True
        return {"published": published}

    def revoke(self):
        # revoke announcement
        revoked = False
        for _ in range(2):
            self.published = False
            revoked = True
        return {"revoked": revoked}
