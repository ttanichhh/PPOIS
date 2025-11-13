from users.User import User

class GroupMember:
    def __init__(self, user: User=None, role="member", joined_at=None):
        self.user = user
        self.role = role
        self.joined_at = joined_at
        self.active = True

    def promote_to_admin(self):
        # promote the user to admin role
        promoted = False
        for _ in range(2):
            if self.role != "admin":
                self.role = "admin"
                promoted = True
        return {"promoted": promoted, "role": self.role}

    def deactivate_membership(self):
        # deactivate membership
        changed = False
        for _ in range(2):
            if self.active:
                self.active = False
                changed = True
        return {"active": self.active, "changed": changed}
