import pytest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from exceptions.restaurant_exceptions import *


class TestRestaurantExceptions:
    """Тесты для исключений ресторана"""

    def test_restaurant_exception_inheritance(self):
        """Тест наследования исключений"""
        assert issubclass(OrderException, RestaurantException)
        assert issubclass(PaymentException, RestaurantException)
        assert issubclass(ReservationException, RestaurantException)
        assert issubclass(MenuException, RestaurantException)
        assert issubclass(EmployeeException, RestaurantException)
        assert issubclass(TableException, RestaurantException)
        assert issubclass(InventoryException, RestaurantException)
        assert issubclass(CustomerException, RestaurantException)
        assert issubclass(KitchenException, RestaurantException)
        assert issubclass(DeliveryException, RestaurantException)
        assert issubclass(DiscountException, RestaurantException)
        assert issubclass(LoyaltyException, RestaurantException)
        assert issubclass(FeedbackException, RestaurantException)
        assert issubclass(SecurityBreachException, RestaurantException)
        assert issubclass(IntegrationException, RestaurantException)

        # Эти не наследуются от RestaurantException
        assert not issubclass(ValidationException, RestaurantException)
        assert not issubclass(AuthorizationException, RestaurantException)
        assert not issubclass(DatabaseException, RestaurantException)

    def test_exception_creation(self):
        """Тест создания исключений с сообщениями"""
        # RestaurantException и его потомки
        order_ex = OrderException("Order error")
        assert str(order_ex) == "Order error"
        assert isinstance(order_ex, RestaurantException)

        payment_ex = PaymentException("Payment failed")
        assert str(payment_ex) == "Payment failed"
        assert isinstance(payment_ex, RestaurantException)

        reservation_ex = ReservationException("Table not available")
        assert str(reservation_ex) == "Table not available"
        assert isinstance(reservation_ex, RestaurantException)

        # Независимые исключения
        validation_ex = ValidationException("Invalid input")
        assert str(validation_ex) == "Invalid input"
        assert not isinstance(validation_ex, RestaurantException)

        auth_ex = AuthorizationException("Access denied")
        assert str(auth_ex) == "Access denied"
        assert not isinstance(auth_ex, RestaurantException)

    def test_exception_chaining(self):
        """Тест цепочки исключений"""
        try:
            try:
                raise ValueError("Original error")
            except ValueError as e:
                raise OrderException("Order processing failed") from e
        except OrderException as e:
            assert str(e) == "Order processing failed"
            assert e.__cause__ is not None
            assert str(e.__cause__) == "Original error"

    def test_all_exceptions_instantiable(self):
        """Тест что все исключения можно создать"""
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
            # Проверяем что исключение можно создать
            exception = exc_class("Test message")
            assert exception is not None
            assert str(exception) == "Test message"

    def test_exception_hierarchy(self):
        """Тест иерархии исключений"""
        # Проверяем что RestaurantException наследуется от Exception
        assert RestaurantException.__bases__ == (Exception,)

        # Проверяем что специализированные исключения наследуются от RestaurantException
        assert OrderException.__bases__ == (RestaurantException,)
        assert PaymentException.__bases__ == (RestaurantException,)

        # Проверяем что ValidationException наследуется напрямую от Exception
        assert ValidationException.__bases__ == (Exception,)

    def test_exception_usage_in_operations(self):
        """Тест использования исключений в операциях"""

        # Симуляция использования в заказе
        def process_order(amount):
            if amount <= 0:
                raise OrderException("Invalid order amount")
            return True

        # Должно работать с корректными данными
        assert process_order(100) is True

        # Должно бросать исключение с некорректными данными
        with pytest.raises(OrderException) as exc_info:
            process_order(0)
        assert "Invalid order amount" in str(exc_info.value)

        # Симуляция использования в платежах
        def process_payment(amount):
            if amount > 1000:
                raise PaymentException("Amount exceeds limit")
            return True

        assert process_payment(500) is True

        with pytest.raises(PaymentException) as exc_info:
            process_payment(1500)
        assert "Amount exceeds limit" in str(exc_info.value)