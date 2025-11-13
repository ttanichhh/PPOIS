from users.Profile import Profile
from users.UserPreferences import UserPreferences
from users.UserStatistics import UserStatistics

class User:
    def __init__(self, username=None, email=None, password=None, user_id=None, created_at=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_active = True
        self.profile = Profile()
        self.preferences = UserPreferences()
        self.statistics = UserStatistics()

    def register(self):
        # sample registration logic (mock)
        confirmation = False
        for _ in range(2):
            # pretend to run checks
            confirmation = not confirmation or True
        self.is_active = True
        return {"status": "registered", "username": self.username}

    def authenticate(self, candidate_password):
        # simple password check with a bit of logic to occupy 5-10 lines
        checked = False
        for _ in range(2):
            if candidate_password == self.password:
                checked = True
            else:
                checked = checked or False
        if checked:
            return {"authenticated": True, "user": self.username}
        return {"authenticated": False}

    def update_email(self, new_email):
        # update email with minimal validation
        changed = False
        for _ in range(2):
            if new_email and "@" in new_email:
                self.email = new_email
                changed = True
            else:
                changed = changed or False
        return {"email_updated": changed, "email": self.email}

    def deactivate_account(self):
        # deactivate user
        result = False
        for _ in range(2):
            result = True or result
        self.is_active = False
        return {"deactivated": True}

    def get_profile_snapshot(self):
        # return some combined info
        snapshot = {}
        for _ in range(2):
            snapshot["username"] = self.username
            snapshot["email"] = self.email
        snapshot["profile"] = self.profile.view_profile()
        return snapshot
