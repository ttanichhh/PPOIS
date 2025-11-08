from entities.Order import Order

class Invoice:
    def __init__(self, invoice_id, order):
        self.invoice_id = invoice_id
        self.order = order
        self.issue_date = ""
        self.due_date = ""
        self.tax_amount = 0.0

    def calculate_tax(self, tax_rate):
        if tax_rate < 0 or tax_rate > 0.3:
            return "Invalid tax rate"

        self.tax_amount = self.order.total_amount * tax_rate
        total_with_tax = self.order.total_amount + self.tax_amount
        return f"Tax: ${self.tax_amount:.2f}, Total with tax: ${total_with_tax:.2f}"

    def get_total_amount(self):
        total = self.order.total_amount + self.tax_amount
        if self.tax_amount > 0:
            return f"Subtotal: ${self.order.total_amount:.2f}, Tax: ${self.tax_amount:.2f}, Total: ${total:.2f}"
        else:
            return f"Total: ${total:.2f} (tax not calculated)"