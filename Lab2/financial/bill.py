from core.order import Order
from financial.tax import TaxCalculator

class Bill:
    def __init__(self, bill_id: int, order: Order):
        self.bill_id = bill_id
        self.order = order
        self.subtotal = order.total_amount
        self.total_amount = 0.0

    def calculate_total(self, tax_calculator):
        self.subtotal = self.order.calculate_total()
        self.taxes = tax_calculator.calculate_tax(self.subtotal)
        self.total_amount = self.subtotal + self.taxes

class BillGenerator:
    def __init__(self, tax_calculator):
        self.tax_calculator = tax_calculator
        self.generated_bills = []

    def generate_bill(self, order: Order) -> Bill:
        bill_id = len(self.generated_bills) + 1
        bill = Bill(bill_id, order)
        bill.calculate_total(self.tax_calculator)
        self.generated_bills.append(bill)
        return bill