class Shift:
    def __init__(self, shift_id: int, start_time: str, end_time: str, shift_type: str):
        self.shift_id = shift_id
        self.start_time = start_time
        self.end_time = end_time
        self.shift_type = shift_type
        self.employees = []