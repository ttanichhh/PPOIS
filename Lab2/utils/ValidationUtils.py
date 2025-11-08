class ValidationUtils:
    def __init__(self):
        self.validation_rules = {}

    def validate_email(self, email):
        if not email or "@" not in email:
            return "❌ Invalid email: missing @ symbol"

        parts = email.split("@")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return "❌ Invalid email format"

        domain = parts[1]
        if "." not in domain:
            return "❌ Invalid email: missing domain extension"

        common_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
        if domain in common_domains:
            return f"✅ Valid email ({domain} is common)"
        else:
            return f"✅ Valid email (custom domain: {domain})"

    def validate_phone(self, phone):
        if not phone:
            return "❌ Phone number cannot be empty"

        # Remove common separators
        clean_phone = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

        if not clean_phone.isdigit():
            return "❌ Phone number must contain only digits"

        if len(clean_phone) == 10:
            return "✅ Valid 10-digit phone number"
        elif len(clean_phone) == 11 and clean_phone[0] == '1':
            return "✅ Valid 11-digit US phone number"
        else:
            return f"❌ Invalid phone length: {len(clean_phone)} digits"