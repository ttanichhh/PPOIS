from core.employee import Employee

class Payroll:
    def __init__(self, payroll_id: int, employee: Employee, period_start: str, period_end: str):
        self.payroll_id = payroll_id
        self.employee = employee
        self.period_start = period_start
        self.period_end = period_end
        self.base_salary = employee.salary
        self.net_pay = 0.0

    def calculate_net_pay(self):
        self.net_pay = self.base_salary * 0.8

class PayrollSystem:
    def __init__(self):
        self.payroll_records = []

    def process_payroll(self, employees: list, period_start: str, period_end: str):
        for employee in employees:
            payroll = Payroll(len(self.payroll_records) + 1, employee, period_start, period_end)
            payroll.calculate_net_pay()
            self.payroll_records.append(payroll)
        return self.payroll_records