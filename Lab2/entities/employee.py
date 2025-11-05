class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = 0.0
        self.hire_date = ""

    def calculate_bonus(self, performance_rating):
        bonus = self.salary * 0.1 * performance_rating
        return bonus

    def get_employee_details(self):
        return f"{self.name} - {self.position}"