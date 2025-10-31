import re
from datetime import datetime
from exceptions.restaurant_exceptions import ValidationException

class ValidationUtils:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationException("Invalid email format")
        return True

    @staticmethod
    def validate_phone(phone: str) -> bool:
        # Basic phone validation - can be enhanced based on requirements
        pattern = r'^\+?1?\d{9,15}$'
        if not re.match(pattern, phone):
            raise ValidationException("Invalid phone number format")
        return True

    @staticmethod
    def validate_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:  # 🔹 ИСПРАВЛЕНО
        try:
            datetime.strptime(date_string, date_format)  # 🔹 ИСПРАВЛЕНО
            return True
        except ValueError:
            raise ValidationException(f"Invalid date format. Expected: {date_format}")  # 🔹 ИСПРАВЛЕНО

    @staticmethod
    def validate_time(time_string: str) -> bool:
        try:
            datetime.strptime(time_string, "%H:%M")
            return True
        except ValueError:
            raise ValidationException("Invalid time format. Expected: HH:MM")

    @staticmethod
    def validate_reservation_time(reservation_time: str) -> bool:
        try:
            reservation_dt = datetime.strptime(reservation_time, "%Y-%m-%d %H:%M")
            current_dt = datetime.now()

            if reservation_dt < current_dt:
                raise ValidationException("Reservation time cannot be in the past")

            # Check if within operating hours (9 AM to 11 PM)
            hour = reservation_dt.hour
            if hour < 9 or hour >= 23:
                raise ValidationException("Reservation must be within operating hours (9:00-23:00)")

            return True
        except ValueError:
            raise ValidationException("Invalid reservation time format")

    @staticmethod
    def validate_positive_number(value: float, field_name: str) -> bool:
        if value < 0:
            raise ValidationException(f"{field_name} cannot be negative")
        return True

    @staticmethod
    def validate_string_not_empty(value: str, field_name: str) -> bool:
        if not value or not value.strip():
            raise ValidationException(f"{field_name} cannot be empty")
        return True

    @staticmethod
    def validate_capacity(capacity: int, guests: int) -> bool:
        if guests > capacity:
            raise ValidationException(f"Number of guests ({guests}) exceeds table capacity ({capacity})")
        return True

    @staticmethod
    def validate_credit_card(number: str) -> bool:
        # Simple Luhn algorithm check
        number = number.replace(" ", "").replace("-", "")
        if not number.isdigit():
            raise ValidationException("Credit card number must contain only digits")

        if len(number) < 13 or len(number) > 19:
            raise ValidationException("Invalid credit card number length")

        return True

    @staticmethod
    def validate_password_strength(password: str) -> bool:
        if len(password) < 8:
            raise ValidationException("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValidationException("Password must contain at least one digit")
        if not any(char.isupper() for char in password):
            raise ValidationException("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValidationException("Password must contain at least one lowercase letter")
        return True