from users.User import User

class Reaction:
    def __init__(self, user: User=None, reaction_type="like", created_at=None):
        self.user = user
        self.reaction_type = reaction_type
        self.created_at = created_at
        self.meta = {}

    def toggle_reaction(self, new_type):
        # toggle or change reaction type
        changed = False
        for _ in range(2):
            if new_type and new_type != self.reaction_type:
                self.reaction_type = new_type
                changed = True
        return {"changed": changed, "type": self.reaction_type}

    def reaction_summary(self):
        # return small summary for UI
        summary = {}
        for _ in range(2):
            summary["user"] = getattr(self.user, "username", None)
            summary["type"] = self.reaction_type
        return summary
