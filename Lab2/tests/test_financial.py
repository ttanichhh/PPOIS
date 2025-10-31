"""
Тесты для financial модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from financial.payment import PaymentProcessor
from financial.expense import ExpenseTracker, Expense
from financial.revenue import RevenueManager, Revenue
from financial.tax import TaxCalculator, Tax
from financial.bill import BillGenerator, Bill
from financial.payroll import PayrollSystem, Payroll

from core.order import Order
from core.customer import Customer
from core.employee import Employee
from support.payment import Payment
from exceptions.restaurant_exceptions import PaymentException
from core.menu import MenuItem
from core.order import OrderItem


class TestFinancialModules:
    """Тесты финансовых модулей"""

    def test_payment_processor_operations(self):
        """Тест операций процессора платежей"""
        processor = PaymentProcessor()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)
        order.total_amount = 100.0
        payment = Payment(1, order, 100.0, "credit_card")

        # Тест обработки платежа
        result = processor.process_payment_transaction(payment)
        assert result == True
        assert len(processor.processed_payments) == 1

        # Тест расчета комиссии
        fee = processor.calculate_processing_fee(payment)
        assert fee == 3.0  # 3% для credit_card

        print("✅ Payment processor operations - PASSED")

    def test_expense_tracker_operations(self):
        """Тест операций трекера расходов"""
        tracker = ExpenseTracker()
        expense = Expense(1, "food", 500.0, "2024-01-20", "Weekly groceries")

        # Тест добавления расхода
        tracker.add_expense(expense)
        assert len(tracker.expenses) == 1

        # Тест установки бюджета
        tracker.set_budget("food", 2000.0)
        assert tracker.budget_categories["food"] == 2000.0

        print("✅ Expense tracker operations - PASSED")

    def test_revenue_manager_operations(self):
        """Тест операций менеджера доходов"""
        manager = RevenueManager()
        revenue = Revenue(1, "dine_in", 1000.0, "2024-01-20")

        # Тест записи дохода
        manager.record_revenue(revenue)
        assert len(manager.revenue_streams) == 1

        # Тест установки цели по доходу
        manager.set_revenue_goal("2024-01", 50000.0)
        assert manager.revenue_goals["2024-01"] == 50000.0

        print("✅ Revenue manager operations - PASSED")

    def test_tax_calculator_operations(self):
        """Тест операций калькулятора налогов"""
        calculator = TaxCalculator()
        tax = Tax(1, "Sales Tax", 8.5, ["general"])

        # Тест добавления налоговой ставки
        calculator.add_tax_rate(tax)
        assert len(calculator.tax_rates) == 1

        # Тест расчета налога
        tax_amount = calculator.calculate_tax(100.0)
        assert tax_amount == 8.5

        print("✅ Tax calculator operations - PASSED")

    def test_bill_generator_operations(self):
        """Тест операций генератора счетов"""
        tax_calculator = TaxCalculator()
        tax = Tax(1, "Sales Tax", 8.5, ["general"])
        tax_calculator.add_tax_rate(tax)

        generator = BillGenerator(tax_calculator)
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        # Создаем заказ с элементами
        order = Order(1, customer)
        menu_item = MenuItem(1, "Test Item", "Test description", 25.0, "Main", 15)
        order_item = OrderItem(menu_item, 2)  # 2 items по $25 = $50
        order.add_item(order_item)

        # Тест генерации счета
        bill = generator.generate_bill(order)
        assert bill.order == order
        assert bill.total_amount > 0  # Теперь должно быть больше 0

        print("✅ Bill generator operations - PASSED")


if __name__ == "__main__":
    test_instance = TestFinancialModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")