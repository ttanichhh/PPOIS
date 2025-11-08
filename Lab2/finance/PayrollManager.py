from entities.Employee import Employee


class PayrollManager:
    def __init__(self):
        self.employees = []
        self.pay_period = ""

    def calculate_salary(self, employee):
        if employee.salary <= 0:
            return f"Salary not set for {employee.name}"

        tax_rate = 0.15
        tax_amount = employee.salary * tax_rate
        net_salary = employee.salary - tax_amount

        benefits = {
            "Manager": 500,
            "Chef": 300,
            "Waiter": 100
        }
        benefit_amount = benefits.get(employee.position, 0)

        return f"Salary for {employee.name}:\nGross: ${employee.salary:.2f}\nTax: -${tax_amount:.2f}\nBenefits: +${benefit_amount:.2f}\nNet: ${net_salary + benefit_amount:.2f}"

    def process_payroll(self):
        if not self.employees:
            return "No employees in payroll system"

        total_payroll = sum(emp.salary for emp in self.employees)
        employee_count = len(self.employees)
        avg_salary = total_payroll / employee_count

        payroll_report = f"Payroll Processing - {self.pay_period}\n"
        payroll_report += f"Employees: {employee_count}\n"
        payroll_report += f"Total Payroll: ${total_payroll:.2f}\n"
        payroll_report += f"Average Salary: ${avg_salary:.2f}\n"
        payroll_report += "Payroll processed successfully"
        return payroll_report