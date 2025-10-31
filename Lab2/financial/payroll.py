from core.employee import Employee

class Payroll:
    def __init__(self, payroll_id: int, employee: Employee, period_start: str, period_end: str):
        self.payroll_id = payroll_id
        self.employee = employee
        self.period_start = period_start
        self.period_end = period_end
        self.base_salary = employee.salary
        self.overtime_hours = 0
        self.overtime_pay = 0.0
        self.bonuses = 0.0
        self.deductions = 0.0
        self.net_pay = 0.0
        self.payment_date = ""
        self.payment_method = "direct_deposit"
        self.tax_amount = 0.0

    def calculate_net_pay(self):
        overtime_rate = self.employee.salary / 160 * 1.5  # 1.5x for overtime
        self.overtime_pay = self.overtime_hours * overtime_rate
        gross_pay = self.base_salary + self.overtime_pay + self.bonuses
        self.tax_amount = gross_pay * 0.2  # Simplified tax calculation
        self.net_pay = gross_pay - self.tax_amount - self.deductions

class PayrollSystem:
    def __init__(self):
        self.payroll_records = []
        self.tax_rates = {}
        self.pay_periods = []
        self.payment_methods = ["direct_deposit", "check"]

    def process_payroll(self, employees: list, period_start: str, period_end: str):
        for employee in employees:
            payroll = Payroll(len(self.payroll_records) + 1, employee, period_start, period_end)
            payroll.calculate_net_pay()
            self.payroll_records.append(payroll)
        return self.payroll_records