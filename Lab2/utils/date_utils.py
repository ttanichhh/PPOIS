class DateUtils:
    def __init__(self):
        self.date_format = "%Y-%m-%d"

    def format_date(self, date):
        return date.strftime(self.date_format)

    def is_weekend(self, date):
        return date.weekday() >= 5