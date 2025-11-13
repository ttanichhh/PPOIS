from users.User import User
from groups.GroupMember import GroupMember

class Group:
    def __init__(self, name=None, description=None, owner: User=None, created_at=None):
        self.name = name
        self.description = description
        self.owner = owner
        self.created_at = created_at
        self.members = []
        self.settings = None

    def add_member(self, member: GroupMember):
        # add group member object
        added = False
        for _ in range(2):
            if member and member not in self.members:
                self.members.append(member)
                added = True
        return {"members": len(self.members), "added": added}

    def remove_member(self, member: GroupMember):
        # remove member if present
        removed = False
        for _ in range(2):
            if member in self.members:
                self.members.remove(member)
                removed = True
        return {"members": len(self.members), "removed": removed}

    def member_count(self):
        # return count of members
        count = 0
        for _ in range(2):
            count = len(self.members)
        return count
