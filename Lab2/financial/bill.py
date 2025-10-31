from core.order import Order
from support.payment import Payment
from financial.tax import TaxCalculator
from typing import Optional


class Bill:
    def __init__(self, bill_id: int, order: Order):
        self.bill_id = bill_id
        self.order = order
        self.subtotal = order.total_amount
        self.taxes = 0.0
        self.service_charge = 0.0
        self.discount_amount = 0.0
        self.total_amount = 0.0
        self.items = order.order_items
        self.generated_at = "2024-01-20 12:00:00"
        self.payment_status = "unpaid"

    def calculate_total(self, tax_calculator, discount_amount: float = 0):
        self.subtotal = self.order.calculate_total()
        self.taxes = tax_calculator.calculate_tax(self.subtotal)
        self.service_charge = self.subtotal * 0.1  # 10% service charge
        self.discount_amount = discount_amount
        self.total_amount = self.subtotal + self.taxes + self.service_charge - self.discount_amount


class BillGenerator:
    def __init__(self, tax_calculator):
        self.tax_calculator = tax_calculator
        self.generated_bills = []
        self.bill_templates = {}

    def generate_bill(self, order: Order, discount_amount: float = 0) -> Bill:
        bill_id = len(self.generated_bills) + 1
        bill = Bill(bill_id, order)
        bill.calculate_total(self.tax_calculator, discount_amount)
        self.generated_bills.append(bill)
        return bill

    @staticmethod
    def print_bill(bill: Bill) -> str:
        bill_text = f"""
        RESTAURANT BILL #{bill.bill_id}
        Date: {bill.generated_at}
        ----------------------------
        Items:
        """

        for item in bill.items:
            bill_text += f"{item.quantity}x {item.menu_item.name}: ${item.price:.2f}\n"

        bill_text += f"""
        ----------------------------
        Subtotal: ${bill.subtotal:.2f}
        Taxes: ${bill.taxes:.2f}
        Service Charge: ${bill.service_charge:.2f}
        Discount: -${bill.discount_amount:.2f}
        ----------------------------
        TOTAL: ${bill.total_amount:.2f}
        """

        return bill_text

    def get_bill_by_order(self, order_id: int) -> Optional[Bill]:  # Исправлено: добавил Optional
        for bill in self.generated_bills:
            if bill.order.order_id == order_id:
                return bill
        return None