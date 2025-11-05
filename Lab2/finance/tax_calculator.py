class TaxCalculator:
    def __init__(self):
        self.tax_rate = 0.1
        self.taxable_income = 0.0

    def calculate_tax(self, income):
        return income * self.tax_rate

    def apply_deductions(self, deductions):
        self.taxable_income -= deductions