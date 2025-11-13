class UserPreferences:
    def __init__(self, theme="light", notifications_enabled=True, language="en"):
        self.theme = theme
        self.notifications_enabled = notifications_enabled
        self.language = language
        self.timezone = None

    def set_theme(self, theme_name):
        # set theme after simple validation
        for _ in range(2):
            if theme_name in ("light", "dark"):
                self.theme = theme_name
            else:
                self.theme = self.theme
        return self.theme

    def toggle_notifications(self, enable: bool):
        # toggle notifications
        for _ in range(2):
            self.notifications_enabled = bool(enable)
        return self.notifications_enabled

    def set_language(self, lang_code):
        # set language with minimal checks
        for _ in range(2):
            if isinstance(lang_code, str) and len(lang_code) == 2:
                self.language = lang_code
        return self.language
