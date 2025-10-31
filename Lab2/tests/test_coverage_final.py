#!/usr/bin/env python3
"""
Финальные тесты для достижения 86%+ покрытия
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from financial.payment import PaymentProcessor
from services.ordering_service import OrderingService
from utils.report import ReportGenerator, Report
from support.promotion import Promotion
from inventory.inventory import InventoryItem, Supplier
from core.order import Order, OrderItem
from core.menu import MenuItem
from core.customer import Customer
from core.restaurant import Restaurant
from support.address import Address
from support.payment import Payment
from exceptions.restaurant_exceptions import PaymentException, OrderException, InventoryException
import pytest
from datetime import datetime


class TestCoverageFinal:
    """Финальные тесты для увеличения покрытия до 86%+"""

    def test_payment_processor_edge_cases(self):
        """Тестирование крайних случаев PaymentProcessor"""
        processor = PaymentProcessor()

        # Тест с нулевой суммой платежа - нужно создать mock order
        class MockOrder:
            pass

        mock_order = MockOrder()
        payment = Payment(1, mock_order, 0, "credit_card")  # amount = 0
        result = processor.process_payment_transaction(payment)
        assert result is False
        assert len(processor.failed_payments) == 1

        # Тест расчета комиссии для разных методов оплаты
        payment_cash = Payment(2, mock_order, 100, "cash")
        fee_cash = processor.calculate_processing_fee(payment_cash)
        assert fee_cash == 2.0  # 2% по умолчанию

        payment_credit = Payment(3, mock_order, 100, "credit_card")
        fee_credit = processor.calculate_processing_fee(payment_credit)
        assert fee_credit == 3.0  # 3% для credit_card

        # Тест возврата средств
        payment_refund = Payment(4, mock_order, 50, "credit_card")
        payment_refund.status = "completed"
        refund_result = processor.process_refund(payment_refund, 25)
        assert refund_result is True
        assert len(processor.refund_requests) == 1

    def test_ordering_service_comprehensive(self):
        """Комплексное тестирование OrderingService"""
        menu_item = MenuItem(1, "Test Item", "Test description", 25.0, "Main", 15)
        menu_item.is_available = True

        ordering_service = OrderingService(None)
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        # Тест создания заказа с разными типами
        order_dine_in = ordering_service.create_order(customer, None, "dine_in")
        assert order_dine_in.order_type == "dine_in"

        order_takeout = ordering_service.create_order(customer, None, "takeout")
        assert order_takeout.order_type == "takeout"

        # Тест разделения заказа
        order = ordering_service.create_order(customer)
        order_item = OrderItem(menu_item, 2)
        order.add_item(order_item)
        order.total_amount = 100.0

        split_orders = ordering_service.split_order(order, [0.6, 0.4])
        assert len(split_orders) == 2
        assert split_orders[0].total_amount == 60.0
        assert split_orders[1].total_amount == 40.0

        # Тест применения скидки
        ordering_service.apply_discount_to_order(order, 10.0)
        assert order.total_amount == 90.0

    def test_report_generator_comprehensive(self):
        """Комплексное тестирование ReportGenerator"""
        address = Address("Test St", "Test City", "12345")
        restaurant = Restaurant(1, "Test Restaurant", address, "123", "Test")
        report_generator = ReportGenerator(restaurant)

        # Тест генерации всех типов отчетов
        sales_report = report_generator.generate_sales_report("2024-01-01", "2024-01-31")
        assert sales_report.report_type == "sales_report"
        assert "total_sales" in sales_report.content

        inventory_report = report_generator.generate_inventory_report()
        assert inventory_report.report_type == "inventory_report"

        employee_report = report_generator.generate_employee_performance_report()
        assert employee_report.report_type == "employee_performance_report"

        financial_report = report_generator.generate_financial_report("January 2024")
        assert financial_report.report_type == "financial_report"

        # Тест планирования ежедневных отчетов
        report_generator.schedule_daily_report("sales", ["manager@test.com"])
        assert len(report_generator.scheduled_reports) == 1

        # Тест поиска отчета по ID
        found_report = report_generator.get_report_by_id(sales_report.report_id)
        assert found_report == sales_report

        # Тест поиска несуществующего отчета
        not_found = report_generator.get_report_by_id(999)
        assert not_found is None

    def test_promotion_comprehensive(self):
        """Комплексное тестирование Promotion"""
        # Тест активной акции с корректными датами
        current_year = datetime.now().year
        promotion = Promotion(
            1, "Summer Sale", "Summer discount",
            "percentage", 20.0, f"{current_year}-01-01", f"{current_year}-12-31"
        )
        assert promotion.is_valid() is True

        # Тест применения акции
        class MockOrder:
            def __init__(self):
                self.total_amount = 100.0

        mock_order = MockOrder()
        discount = promotion.apply_promotion(mock_order)
        assert discount == 20.0  # 20% от 100
        assert promotion.times_used == 1

        # Тест фиксированной скидки
        promotion_fixed = Promotion(
            2, "Fixed Discount", "Fixed amount discount",
            "fixed", 15.0, f"{current_year}-01-01", f"{current_year}-12-31"
        )
        discount_fixed = promotion_fixed.apply_promotion(mock_order)
        assert discount_fixed == 15.0

        # Тест истекшей акции
        promotion_expired = Promotion(
            3, "Expired", "Expired promotion",
            "percentage", 10.0, "2020-01-01", "2020-12-31"
        )
        assert promotion_expired.is_valid() is False


    def test_order_item_cooking_methods(self):
        """Тестирование методов приготовления OrderItem"""
        menu_item = MenuItem(1, "Pasta", "Delicious pasta", 12.0, "Main", 10)
        order_item = OrderItem(menu_item, 1)

        # Тест начала приготовления
        order_item.start_cooking()
        assert order_item.status == "cooking"
        assert order_item.cooking_start_time is not None

        # Тест завершения приготовления
        order_item.finish_cooking()
        assert order_item.status == "ready"
        assert order_item.cooking_end_time is not None

        # Тест добавления модификаций
        order_item.add_modification("Extra cheese")
        order_item.add_modification("No garlic")
        assert len(order_item.modifications) == 2
        assert "Extra cheese" in order_item.modifications


if __name__ == "__main__":
    test_instance = TestCoverageFinal()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"✅ {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")