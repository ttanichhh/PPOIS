class ValidationUtils:
    def __init__(self):
        self.validation_rules = {}

    def validate_email(self, email):
        return "@" in email

    def validate_phone(self, phone):
        return len(phone) >= 10