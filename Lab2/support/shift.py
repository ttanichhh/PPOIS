from datetime import datetime

class Shift:
    def __init__(self, shift_id: int, start_time: str, end_time: str, shift_type: str):
        self.shift_id = shift_id
        self.start_time = start_time
        self.end_time = end_time
        self.shift_type = shift_type
        self.employees = []
        self.max_employees = 5
        self.min_employees = 2
        self.is_holiday = False
        self.special_notes = ""

    def add_employee(self, employee):
        if len(self.employees) < self.max_employees:
            self.employees.append(employee)
            return True
        return False

    def get_duration_hours(self) -> float:
        start = datetime.strptime(self.start_time, "%H:%M")
        end = datetime.strptime(self.end_time, "%H:%M")
        return (end - start).seconds / 3600