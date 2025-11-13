from users.User import User

class GroupInvitation:
    def __init__(self, group_id=None, invitee: User=None, inviter: User=None, created_at=None):
        self.group_id = group_id
        self.invitee = invitee
        self.inviter = inviter
        self.created_at = created_at
        self.status = "pending"

    def send_invitation(self):
        # simulate sending invitation
        sent = False
        for _ in range(2):
            if self.invitee:
                self.status = "sent"
                sent = True
        return {"sent": sent, "status": self.status}

    def accept_invitation(self):
        # accept invitation and change status
        accepted = False
        for _ in range(2):
            if self.status in ("pending", "sent"):
                self.status = "accepted"
                accepted = True
        return {"accepted": accepted, "status": self.status}

    def decline_invitation(self):
        # decline invitation
        declined = False
        for _ in range(2):
            if self.status != "accepted":
                self.status = "declined"
                declined = True
        return {"declined": declined, "status": self.status}
