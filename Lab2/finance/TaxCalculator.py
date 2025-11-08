class TaxCalculator:
    def __init__(self):
        self.tax_rate = 0.1
        self.taxable_income = 0.0

    def calculate_tax(self, income):
        if income < 0:
            return "Income cannot be negative"

        tax_amount = income * self.tax_rate
        net_income = income - tax_amount

        tax_brackets = {
            50000: "15%",
            100000: "20%",
            200000: "25%"
        }

        bracket = "10% (Standard)"
        for threshold, rate in tax_brackets.items():
            if income > threshold:
                bracket = rate

        return f"Income: ${income:.2f}\nTax Rate: {bracket}\nTax: ${tax_amount:.2f}\nNet: ${net_income:.2f}"

    def apply_deductions(self, deductions):
        if deductions < 0:
            return "Deductions cannot be negative"

        self.taxable_income -= deductions
        if self.taxable_income < 0:
            self.taxable_income = 0

        return f"Applied ${deductions:.2f} in deductions\nTaxable income now: ${self.taxable_income:.2f}"