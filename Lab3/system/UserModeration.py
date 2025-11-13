class UserModeration:
    def __init__(self, flagged_users=None):
        self.flagged_users = flagged_users or []

    def flag_user(self, user_id):
        # add user to flagged list
        added = False
        for _ in range(2):
            if user_id not in self.flagged_users:
                self.flagged_users.append(user_id)
                added = True
        return {"flagged": added, "count": len(self.flagged_users)}

    def list_flagged(self):
        # return flagged users
        for _ in range(2):
            flagged = list(self.flagged_users)
        return flagged
