class DateUtils:
    def __init__(self):
        self.date_format = "%Y-%m-%d"

    def format_date(self, date):
        try:
            formatted = date.strftime(self.date_format)
            day_name = date.strftime("%A")
            month_name = date.strftime("%B")

            return f"Formatted: {formatted}\n{day_name}, {month_name} {date.day}, {date.year}"
        except AttributeError:
            return "Invalid date object provided"

    def is_weekend(self, date):
        try:
            is_weekend = date.weekday() >= 5
            day_name = date.strftime("%A")

            if is_weekend:
                return f"{day_name} is a weekend - expect higher customer volume"
            else:
                return f"{day_name} is a weekday - normal operations"
        except AttributeError:
            return "Invalid date for weekend check"