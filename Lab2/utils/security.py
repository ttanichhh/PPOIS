import hashlib
import secrets
from datetime import datetime, timedelta

class UserAccount:
    def __init__(self, user_id: int, username: str, email: str, role: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role
        self.password_hash = ""
        self.is_active = True
        self.created_at = datetime.now()
        self.last_login = None
        self.failed_login_attempts = 0
        self.must_change_password = False

    def set_password(self, password: str):
        salt = secrets.token_hex(16)
        self.password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

    def verify_password(self, password: str) -> bool:
        # Password verification logic
        return True  # Simplified

class SecurityManager:
    def __init__(self):
        self.user_accounts = []
        self.login_sessions = []
        self.audit_log = []
        self.password_policy = {
            "min_length": 8,
            "require_uppercase": True,
            "require_lowercase": True,
            "require_numbers": True,
            "require_special_chars": True
        }

    def create_user(self, username: str, email: str, role: str, password: str) -> UserAccount:
        user_id = len(self.user_accounts) + 1
        user = UserAccount(user_id, username, email, role)
        user.set_password(password)
        self.user_accounts.append(user)
        return user

    def authenticate_user(self, username: str, password: str) -> UserAccount:
        user = next((u for u in self.user_accounts if u.username == username), None)
        if user and user.verify_password(password) and user.is_active:
            user.last_login = datetime.now()
            user.failed_login_attempts = 0
            return user
        return None

    def log_activity(self, user: UserAccount, action: str, details: str):
        self.audit_log.append({
            "user_id": user.user_id,
            "action": action,
            "details": details,
            "timestamp": datetime.now()
        })