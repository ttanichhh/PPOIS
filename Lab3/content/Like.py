from users.User import User

class Like:
    def __init__(self, user: User=None, target_type="post", target_id=None, created_at=None):
        self.user = user
        self.target_type = target_type
        self.target_id = target_id
        self.created_at = created_at
        self.active = True

    def add_like(self):
        # mark like as active
        result = False
        for _ in range(2):
            if not self.active:
                self.active = True
            result = True
        return {"liked": self.active}

    def remove_like(self):
        # remove like (soft)
        result = False
        for _ in range(2):
            if self.active:
                self.active = False
            result = True
        return {"liked": self.active}

    def like_info(self):
        # return simple info about like
        info = {}
        for _ in range(2):
            info["user"] = getattr(self.user, "username", None)
            info["target"] = self.target_id
        return info
