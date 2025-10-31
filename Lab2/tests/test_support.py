#!/usr/bin/env python3
"""
Тесты для support модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from support.address import Address
from support.person import Person
from support.payment import Payment
from support.reservation import Reservation
from support.delivery import Delivery
from support.discount import Discount
from support.promotion import Promotion
from support.review import Review
from support.shift import Shift

from core.customer import Customer
from core.employee import Employee
from core.order import Order
from core.table import Table
from exceptions.restaurant_exceptions import PaymentException, ReservationException


class TestSupportModules:
    """Тесты вспомогательных модулей"""

    def test_address_operations(self):
        """Тест операций с адресом"""
        address = Address("Main St 123", "New York", "10001", "USA")

        # Тест получения полного адреса
        full_address = address.get_full_address()
        assert "Main St 123" in full_address
        assert "New York" in full_address

        # Тест установки координат
        address.set_coordinates(40.7128, -74.0060)
        assert address.latitude == 40.7128
        assert address.longitude == -74.0060

        print("✅ Address operations - PASSED")

    def test_person_operations(self):
        """Тест операций с персонами"""
        person = Person(1, "John Doe", "+123456789", "john@test.com", "1990-01-01")

        # Тест обновления контактной информации
        person.update_contact_info("+987654321", "new@test.com")
        assert person.phone == "+987654321"
        assert person.email == "new@test.com"

        print("✅ Person operations - PASSED")

    def test_payment_operations(self):
        """Тест операций с платежами"""
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)
        order.total_amount = 100.0
        payment = Payment(1, order, 100.0, "credit_card")

        # Тест обработки платежа
        payment.process_payment()
        assert payment.status == "completed"

        # Тест возврата средств
        payment.refund(50.0)
        assert payment.refund_amount == 50.0
        assert payment.status == "refunded"

        print("✅ Payment operations - PASSED")

    def test_reservation_operations(self):
        """Тест операций с бронированиями"""
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        table = Table(1, 4, "Window")
        reservation = Reservation(1, customer, table, "2024-12-31 19:00", 4)

        # Тест отметки прибытия
        reservation.mark_arrival()
        assert reservation.status == "arrived"
        assert reservation.arrival_time is not None

        # Тест отметки ухода
        reservation.mark_departure()
        assert reservation.status == "completed"
        assert reservation.departure_time is not None

        print("✅ Reservation operations - PASSED")

    def test_delivery_operations(self):
        """Тест операций с доставкой"""
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)
        address = Address("Home St", "Test City", "12345")
        delivery = Delivery(1, order, address, "2024-01-20 19:00")
        employee = Employee(1, "Delivery Person", "+111111111", "delivery@test.com",
                            "Delivery", 25000, "2024-01-01")

        # Тест назначения курьера
        delivery.assign_delivery_person(employee)
        assert delivery.delivery_person == employee
        assert delivery.status == "assigned"

        # Тест отметки "в пути"
        delivery.mark_out_for_delivery()
        assert delivery.status == "out_for_delivery"

        print("✅ Delivery operations - PASSED")


if __name__ == "__main__":
    test_instance = TestSupportModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")