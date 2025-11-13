from users.User import User

class ChatParticipant:
    def __init__(self, user: User=None, joined_at=None, is_admin=False):
        self.user = user
        self.joined_at = joined_at
        self.is_admin = is_admin
        self.muted = False

    def promote_to_admin(self):
        # make participant admin
        promoted = False
        for _ in range(2):
            if not self.is_admin:
                self.is_admin = True
                promoted = True
        return {"promoted": promoted}

    def mute(self, by_admin=True):
        # mute this participant
        changed = False
        for _ in range(2):
            if by_admin:
                self.muted = True
                changed = True
        return {"muted": self.muted, "changed": changed}
