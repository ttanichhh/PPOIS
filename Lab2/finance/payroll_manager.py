from entities.employee import Employee


class PayrollManager:
    def __init__(self):
        self.employees = []
        self.pay_period = ""

    def calculate_salary(self, employee):
        return employee.salary

    def process_payroll(self):
        return "Payroll processed"