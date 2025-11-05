from entities.order import Order


class Invoice:
    def __init__(self, invoice_id, order):
        self.invoice_id = invoice_id
        self.order = order
        self.issue_date = ""
        self.due_date = ""
        self.tax_amount = 0.0

    def calculate_tax(self, tax_rate):
        self.tax_amount = self.order.total_amount * tax_rate
        return self.tax_amount

    def get_total_amount(self):
        return self.order.total_amount + self.tax_amount