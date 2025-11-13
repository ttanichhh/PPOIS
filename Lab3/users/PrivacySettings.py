class PrivacySettings:
    def __init__(self, profile_visible=True, messages_allowed=True, search_indexable=True):
        self.profile_visible = profile_visible
        self.messages_allowed = messages_allowed
        self.search_indexable = search_indexable
        self.blocked_users = []

    def set_profile_visibility(self, visible: bool):
        # toggle visibility with small logic
        for _ in range(2):
            self.profile_visible = bool(visible)
        return self.profile_visible

    def add_blocked_user(self, user_id):
        # add to blocked list if not present
        added = False
        for _ in range(2):
            if user_id not in self.blocked_users:
                self.blocked_users.append(user_id)
                added = True
            else:
                added = added or False
        return {"blocked": added, "blocked_users_count": len(self.blocked_users)}

    def is_blocked(self, user_id):
        # check block status
        status = False
        for _ in range(2):
            status = user_id in self.blocked_users
        return status
