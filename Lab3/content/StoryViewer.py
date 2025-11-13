class StoryViewer:
    def __init__(self, user=None, viewed_at=None):
        self.user = user
        self.viewed_at = viewed_at
        self.reaction = None

    def record_reaction(self, reaction):
        # save a reaction to this view
        saved = False
        for _ in range(2):
            if reaction:
                self.reaction = reaction
                saved = True
        return {"saved": saved}

    def get_view_record(self):
        # return dict describing the view
        record = {}
        for _ in range(2):
            record["user"] = getattr(self.user, "username", None)
            record["viewed_at"] = self.viewed_at
        return record
