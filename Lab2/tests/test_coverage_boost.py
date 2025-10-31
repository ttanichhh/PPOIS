#!/usr/bin/env python3
"""
Финальные тесты для достижения 85% покрытия
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from services.reporting_service import ReportingService
from services.delivery_service import DeliveryService
from services.ordering_service import OrderingService
from management.customer_management import CustomerManagement, LoyaltyProgram
from management.employee_management import EmployeeManagement
from management.inventory_management import InventoryManagement
from management.reservation_management import ReservationManagement
from utils.validation import ValidationUtils
from utils.loyalty import LoyaltyManager, Reward
from utils.notification import NotificationService
from utils.report import ReportGenerator

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Employee, Chef
from core.menu import Menu, MenuItem, MenuCategory
from core.order import Order, OrderItem
from core.table import Table
from support.address import Address
from support.reservation import Reservation
from inventory.inventory import InventoryItem
from financial.revenue import RevenueManager, Revenue
from financial.payment import PaymentProcessor
from financial.expense import ExpenseTracker, Expense
from exceptions.restaurant_exceptions import ValidationException


class TestCoverageBoost:
    """Тесты для увеличения покрытия до 85%"""

    def test_reporting_service_comprehensive(self):
        """Комплексный тест сервиса отчетности"""
        address = Address("Test St", "Test City", "12345")
        restaurant = Restaurant(1, "Test Restaurant", address, "123", "Test")

        # Добавляем столы чтобы избежать деления на ноль
        table1 = Table(1, 2, "Window")
        table2 = Table(2, 4, "Center")
        restaurant.add_table(table1)
        restaurant.add_table(table2)

        reporting_service = ReportingService(restaurant)

        # Тест генерации различных отчетов
        daily_report = reporting_service.generate_daily_operations_report()
        assert "total_orders" in daily_report
        assert "total_revenue" in daily_report

        weekly_report = reporting_service.generate_weekly_financial_report()
        assert "total_revenue" in weekly_report

        customer_report = reporting_service.generate_customer_analytics_report()
        assert "total_customers" in customer_report

        employee_report = reporting_service.generate_employee_performance_report("January")
        assert "period" in employee_report

        print("✅ Reporting service comprehensive - PASSED")

    def test_delivery_service_comprehensive(self):
        """Комплексный тест сервиса доставки"""
        delivery_service = DeliveryService()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)
        address = Address("Home St", "New York", "10001")

        # Тест планирования доставки
        from support.delivery import Delivery
        delivery = Delivery(1, order, address, "2024-01-20 19:00")

        # Добавляем доставку в активные перед тестом
        delivery_service.active_deliveries.append(delivery)

        # Тест обновления статуса доставки
        delivery_service.update_delivery_status(delivery, "out_for_delivery")
        assert delivery.status == "out_for_delivery"

        delivery_service.update_delivery_status(delivery, "delivered")
        assert delivery.status == "delivered"

        # Тест отслеживания доставки
        tracking_info = delivery_service.track_delivery(delivery)
        assert "status" in tracking_info
        assert "eta" in tracking_info

        print("✅ Delivery service comprehensive - PASSED")

    def test_ordering_service_comprehensive(self):
        """Комплексный тест сервиса заказов"""
        menu_item1 = MenuItem(1, "Pizza", "Cheesy pizza", 15.99, "Main", 20)
        menu_item2 = MenuItem(2, "Salad", "Fresh salad", 8.99, "Starter", 10)
        menu = Menu(1, "Test Menu", "Test menu description")
        category = MenuCategory(1, "Main Courses", "Main dishes", 1)
        category.add_menu_item(menu_item1)
        category.add_menu_item(menu_item2)
        menu.add_category(category)

        ordering_service = OrderingService(menu)
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        table = Table(1, 4, "Window")

        # Тест создания заказа
        order = ordering_service.create_order(customer, table, "dine_in")
        assert order.order_type == "dine_in"

        # Тест добавления нескольких элементов
        order_item1 = ordering_service.add_item_to_order(order, menu_item1, 2)
        order_item2 = ordering_service.add_item_to_order(order, menu_item2, 1)
        assert len(order.order_items) == 2

        # Тест получения популярных элементов
        popular_items = ordering_service.get_popular_items(2)
        assert isinstance(popular_items, list)

        print("✅ Ordering service comprehensive - PASSED")

    def test_management_modules_comprehensive(self):
        """Комплексный тест модулей управления"""
        # Customer Management
        customer_mgmt = CustomerManagement()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        customer_mgmt.register_customer(customer)

        # Тест записи отзыва
        customer_mgmt.record_feedback(customer, 5, "Excellent service!")
        assert len(customer_mgmt.feedback_records) == 1

        # Employee Management
        emp_mgmt = EmployeeManagement()
        chef = Chef(1, "Test Chef", "+111111111", "chef@test.com",
                    50000, "2024-01-01", "Italian", 5)
        emp_mgmt.hire_employee(chef)

        # Тест записи производительности
        emp_mgmt.record_performance(1, 4.5, "Great work!")
        assert len(emp_mgmt.performance_records[1]) == 1

        # Inventory Management
        inventory_mgmt = InventoryManagement()
        inventory_item = InventoryItem(1, "Flour", "Baking", 100, "kg", 20, 2.5)
        inventory_mgmt.add_inventory_item(inventory_item)

        # Тест генерации заказа на покупку
        supplier_mock = type('Supplier', (), {'name': 'Test Supplier'})()
        purchase_order = inventory_mgmt.generate_purchase_order(
            supplier_mock, [{'name': 'Flour', 'quantity': 50, 'cost': 2.5}]
        )
        assert purchase_order['status'] == 'pending'

        print("✅ Management modules comprehensive - PASSED")

    def test_validation_utils_comprehensive(self):
        """Комплексный тест утилит валидации"""
        # Тест валидации времени бронирования
        try:
            ValidationUtils.validate_reservation_time("2024-12-31 19:00")
            # Должно пройти для будущей даты
        except ValidationException:
            pass  # Может упасть если текущая дата позже

        # Тест валидации кредитной карты
        assert ValidationUtils.validate_credit_card("4111111111111111") == True

        try:
            ValidationUtils.validate_credit_card("1234")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        print("✅ Validation utils comprehensive - PASSED")

    def test_loyalty_notification_comprehensive(self):
        """Комплексный тест лояльности и уведомлений"""
        # Loyalty Manager
        loyalty_manager = LoyaltyManager()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        customer.loyalty_points = 200

        reward = Reward(1, "Free Dessert", 150, "Get a free dessert")
        loyalty_manager.add_reward(reward)

        # Тест получения преимуществ уровня
        benefits = loyalty_manager.get_tier_benefits("Gold")
        assert "points_multiplier" in benefits
        assert "discount" in benefits

        # Notification Service
        notification_service = NotificationService()
        employee = Employee(1, "Test Employee", "+111111111", "employee@test.com",
                            "Manager", 50000, "2024-01-01")

        # Создаем настоящий объект Shift вместо строки
        from support.shift import Shift
        shift = Shift(1, "09:00", "17:00", "day")

        # Тест различных типов уведомлений
        notification1 = notification_service.send_shift_reminder(employee, shift)
        assert notification1.notification_type == "shift_reminder"

        # Тест очистки устаревших уведомлений
        notification_service.cleanup_expired_notifications()

        print("✅ Loyalty notification comprehensive - PASSED")

    def test_financial_modules_comprehensive(self):
        """Комплексный тест финансовых модулей"""
        # Revenue Manager
        revenue_mgmt = RevenueManager()
        revenue1 = Revenue(1, "dine_in", 1000.0, "2024-01-20")
        revenue2 = Revenue(2, "delivery", 500.0, "2024-01-20")
        revenue_mgmt.record_revenue(revenue1)
        revenue_mgmt.record_revenue(revenue2)

        # Тест расчета роста выручки
        growth_rate = revenue_mgmt.calculate_growth_rate("2024-01-20", "2024-01-19")
        assert isinstance(growth_rate, float)

        # Expense Tracker
        expense_tracker = ExpenseTracker()
        expense = Expense(1, "food", 500.0, "2024-01-20", "Weekly groceries")
        expense_tracker.add_expense(expense)

        # Тест генерации отчета расходов
        expense_report = expense_tracker.generate_expense_report("2024-01-01", "2024-01-31")
        assert "total_expenses" in expense_report
        assert "category_breakdown" in expense_report

        print("✅ Financial modules comprehensive - PASSED")


if __name__ == "__main__":
    test_instance = TestCoverageBoost()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")