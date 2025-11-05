from entities.payment import Payment


class Cashier:
    def __init__(self, cashier_id, name):
        self.cashier_id = cashier_id
        self.name = name
        self.register_balance = 0.0

    def process_cash_payment(self, payment):
        payment.process_payment()
        self.register_balance += payment.amount
        return f"Cash payment processed: ${payment.amount:.2f}"

    def get_register_balance(self):
        return self.register_balance