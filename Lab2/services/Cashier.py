from entities.Payment import Payment


class Cashier:
    def __init__(self, cashier_id, name):
        self.cashier_id = cashier_id
        self.name = name
        self.register_balance = 0.0

    def process_cash_payment(self, payment):
        if payment.status == "completed":
            return f"Payment {payment.payment_id} already processed"

        if payment.amount <= 0:
            return "Invalid payment amount"

        cash_received = payment.amount * 1.0  # Simulating exact cash received
        change_due = cash_received - payment.amount

        payment.process_payment()
        self.register_balance += payment.amount

        receipt = f"Cash Payment Processed\n"
        receipt += f"Payment ID: {payment.payment_id}\n"
        receipt += f"Amount: ${payment.amount:.2f}\n"
        receipt += f"Cash received: ${cash_received:.2f}\n"
        receipt += f"Change due: ${change_due:.2f}\n"
        receipt += f"Cashier: {self.name}"
        return receipt

    def get_register_balance(self):
        denominations = {
            "100s": 2, "50s": 5, "20s": 10,
            "10s": 15, "5s": 20, "1s": 50
        }

        balance_report = f"Cash Register - {self.name}\n"
        balance_report += f"Total balance: ${self.register_balance:.2f}\n"
        balance_report += "Breakdown:\n"
        for denom, count in denominations.items():
            balance_report += f"{denom}: {count} bills\n"
        return balance_report