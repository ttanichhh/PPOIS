"""
Тесты для utils модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from utils.validation import ValidationUtils
from utils.notification import NotificationService, Notification
from utils.loyalty import LoyaltyManager, Reward
from utils.report import ReportGenerator, Report
from utils.security import SecurityManager, UserAccount

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Employee
from support.address import Address
from exceptions.restaurant_exceptions import ValidationException, CustomerException


class TestUtilsModules:
    """Тесты утилитных модулей"""

    def test_validation_utils_comprehensive(self):
        """Комплексный тест утилит валидации"""
        # Тест валидации email
        assert ValidationUtils.validate_email("valid@example.com") == True

        try:
            ValidationUtils.validate_email("invalid")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        # Тест валидации телефона
        assert ValidationUtils.validate_phone("+1234567890") == True

        try:
            ValidationUtils.validate_phone("abc")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        # Тест валидации даты
        assert ValidationUtils.validate_date("2024-01-20") == True

        try:
            ValidationUtils.validate_date("invalid-date")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        # Тест валидации пароля
        assert ValidationUtils.validate_password_strength("StrongPass123") == True

        try:
            ValidationUtils.validate_password_strength("weak")
            assert False, "Should have raised ValidationException"
        except ValidationException:
            pass

        print("✅ Validation utils comprehensive - PASSED")

    def test_notification_service_operations(self):
        """Тест операций сервиса уведомлений"""
        notification_service = NotificationService()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        # Создаем настоящий объект Reservation вместо строки
        from support.reservation import Reservation
        from core.table import Table
        table = Table(1, 4, "Window")
        reservation = Reservation(1, customer, table, "2024-12-31 19:00", 4)

        # Тест отправки уведомления
        notification = notification_service.send_reservation_confirmation(customer, reservation)
        assert notification.recipient == customer
        assert notification.notification_type == "reservation_confirmation"

        # Тест получения непрочитанных уведомлений
        unread = notification_service.get_unread_notifications(customer)
        assert len(unread) == 1

        # Тест отметки как прочитанного
        notification_service.mark_as_read(notification.notification_id)
        unread_after = notification_service.get_unread_notifications(customer)
        assert len(unread_after) == 0

        print("✅ Notification service operations - PASSED")

    def test_loyalty_manager_operations(self):
        """Тест операций менеджера лояльности"""
        loyalty_manager = LoyaltyManager()
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        reward1 = Reward(1, "Free Coffee", 50, "Get a free coffee")
        reward2 = Reward(2, "50% Discount", 100, "50% off your next order")

        loyalty_manager.add_reward(reward1)
        loyalty_manager.add_reward(reward2)

        # Тест начисления баллов (используем существующий метод)
        customer.add_loyalty_points(75)  # Используем метод Customer вместо LoyaltyManager
        assert customer.loyalty_points == 75

        # Тест получения доступных наград
        available_rewards = loyalty_manager.get_available_rewards(customer)
        assert len(available_rewards) == 1  # Only reward1 is affordable

        # Тест обновления уровня клиента
        customer.loyalty_points = 600
        loyalty_manager.update_customer_tier(customer)
        assert customer.membership_tier == "Silver"

        print("✅ Loyalty manager operations - PASSED")

    def test_report_generator_operations(self):
        """Тест операций генератора отчетов"""
        address = Address("Test St", "Test City", "12345")
        restaurant = Restaurant(1, "Test Restaurant", address, "123", "Test")
        report_generator = ReportGenerator(restaurant)

        # Тест генерации отчета продаж
        sales_report = report_generator.generate_sales_report("2024-01-01", "2024-01-31")
        assert sales_report.report_type == "sales_report"
        assert "total_sales" in sales_report.content

        # Тест генерации инвентарного отчета
        inventory_report = report_generator.generate_inventory_report()
        assert inventory_report.report_type == "inventory_report"

        print("✅ Report generator operations - PASSED")

    def test_security_manager_operations(self):
        """Тест операций менеджера безопасности"""
        security_manager = SecurityManager()

        # Тест создания пользователя
        user = security_manager.create_user("testuser", "test@test.com", "manager", "SecurePass123")
        assert user.username == "testuser"
        assert user.role == "manager"

        # Тест аутентификации пользователя
        authenticated_user = security_manager.authenticate_user("testuser", "SecurePass123")
        assert authenticated_user == user

        # Тест логирования активности
        security_manager.log_activity(user, "login", "User logged in")
        assert len(security_manager.audit_log) == 1

        print("✅ Security manager operations - PASSED")


if __name__ == "__main__":
    test_instance = TestUtilsModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")