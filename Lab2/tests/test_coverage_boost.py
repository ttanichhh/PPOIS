import pytest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from exceptions.restaurant_exceptions import *


class TestCoverageBoost:
    """Дополнительные тесты для повышения покрытия"""

    def test_custom_exception_messages(self):
        """Тест кастомных сообщений исключений"""
        messages = {
            OrderException: "Cannot process empty order",
            PaymentException: "Insufficient funds",
            ReservationException: "Table already reserved",
            MenuException: "Item not in menu",
            EmployeeException: "Employee not found",
            TableException: "Table is occupied",
            InventoryException: "Out of stock",
            CustomerException: "Customer not registered",
            KitchenException: "Kitchen is closed",
            DeliveryException: "Delivery zone not supported",
            DiscountException: "Discount code expired",
            LoyaltyException: "Not enough loyalty points",
            FeedbackException: "Invalid rating value",
            SecurityBreachException: "Unauthorized access",
            IntegrationException: "External service unavailable"
        }

        for exc_class, message in messages.items():
            exc = exc_class(message)
            assert str(exc) == message
            assert isinstance(exc, Exception)

    def test_exception_equality(self):
        """Тест сравнения исключений"""
        exc1 = OrderException("Test message")
        exc2 = OrderException("Test message")
        exc3 = OrderException("Different message")

        # Исключения с одинаковым сообщением не равны (разные объекты)
        assert exc1 != exc2
        assert exc1 != exc3

    def test_exception_repr(self):
        """Тест представления исключений"""
        exc = OrderException("Order failed")
        repr_str = repr(exc)
        assert "OrderException" in repr_str
        assert "Order failed" in repr_str

    def test_multiple_inheritance_check(self):
        """Тест что исключения не используют множественное наследование"""
        exceptions = [
            RestaurantException, OrderException, PaymentException,
            ReservationException, MenuException, EmployeeException,
            TableException, InventoryException, CustomerException,
            KitchenException, DeliveryException, DiscountException,
            ValidationException, AuthorizationException, DatabaseException,
            LoyaltyException, FeedbackException, SecurityBreachException,
            IntegrationException
        ]

        for exc_class in exceptions:
            # У каждого исключения должна быть только один базовый класс
            assert len(exc_class.__bases__) == 1

    def test_exception_in_except_blocks(self):
        """Тест использования исключений в блоках except"""
        # OrderException
        try:
            raise OrderException("Order test")
        except OrderException as e:
            assert isinstance(e, OrderException)
            assert str(e) == "Order test"

        # PaymentException
        try:
            raise PaymentException("Payment test")
        except PaymentException as e:
            assert isinstance(e, PaymentException)
            assert str(e) == "Payment test"

        # RestaurantException (базовое)
        try:
            raise RestaurantException("Base test")
        except RestaurantException as e:
            assert isinstance(e, RestaurantException)
            assert str(e) == "Base test"

        # Проверка полиморфизма - OrderException ловится как RestaurantException
        try:
            raise OrderException("Polymorphism test")
        except RestaurantException as e:
            assert isinstance(e, OrderException)
            assert str(e) == "Polymorphism test"