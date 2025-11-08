class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = 0.0
        self.hire_date = ""

    def calculate_bonus(self, performance_rating):
        if performance_rating < 0 or performance_rating > 2:
            return "Invalid rating"

        bonus = self.salary * 0.1 * performance_rating
        if self.position == "Manager":
            bonus *= 1.5
        elif self.position == "Chef":
            bonus *= 1.3

        return f"Bonus: ${bonus:.2f} for {self.name}"

    def get_employee_details(self):
        details = f"{self.name} - {self.position}\n"
        details += f"ID: {self.employee_id}\n"
        details += f"Salary: ${self.salary:.2f}\n"
        details += f"Hire Date: {self.hire_date}"
        return details