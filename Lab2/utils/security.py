class SecurityManager:
    def __init__(self):
        self.user_accounts = []

    def create_user(self, username: str, email: str, role: str) -> dict:
        user = {
            "user_id": len(self.user_accounts) + 1,
            "username": username,
            "email": email,
            "role": role
        }
        self.user_accounts.append(user)
        return user

    def authenticate_user(self, username: str) -> dict:
        return next((u for u in self.user_accounts if u["username"] == username), None)