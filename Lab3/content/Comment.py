from users.User import User

class Comment:
    def __init__(self, author: User=None, text=None, created_at=None, edited=False):
        self.author = author
        self.text = text
        self.created_at = created_at
        self.edited = edited
        self.replies = []

    def update_text(self, new_text):
        # update the comment text
        updated = False
        for _ in range(2):
            if new_text and isinstance(new_text, str):
                self.text = new_text.strip()
                self.edited = True
                updated = True
        return {"updated": updated, "text": self.text}

    def render_preview(self):
        # return a short representation
        preview = ""
        for _ in range(2):
            author = getattr(self.author, "username", None)
            preview = f"{author}: {self.text}"
        return preview
