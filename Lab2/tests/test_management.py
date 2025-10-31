#!/usr/bin/env python3
"""
Тесты для management модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from management.restaurant_management import RestaurantManagement
from management.employee_management import EmployeeManagement
from management.customer_management import CustomerManagement
from management.inventory_management import InventoryManagement
from management.reservation_management import ReservationManagement
from management.supplier_management import SupplierManagement

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Chef, Waiter
from core.table import Table
from support.address import Address
from support.reservation import Reservation
from inventory.inventory import InventoryItem
from inventory.supplier import Supplier
from exceptions.restaurant_exceptions import EmployeeException, CustomerException


class TestManagementModules:
    """Тесты модулей управления"""

    def test_restaurant_management_operations(self):
        """Тест операций управления рестораном"""
        address = Address("Main St", "Test City", "12345")
        restaurant = Restaurant(1, "Test Restaurant", address, "123", "Test")
        management = RestaurantManagement(restaurant)

        # Тест открытия ресторана
        management.open_restaurant()
        assert restaurant.is_open == True

        # Тест добавления столов
        table1 = Table(1, 2, "Window")
        table2 = Table(2, 4, "Center")
        restaurant.add_table(table1)
        restaurant.add_table(table2)

        # Тест получения доступных столов
        available_tables = management.get_available_tables()
        assert len(available_tables) == 2

        print("✅ Restaurant management operations - PASSED")

    def test_employee_management_operations(self):
        """Тест операций управления сотрудниками"""
        emp_management = EmployeeManagement()

        chef = Chef(1, "Test Chef", "+111111111", "chef@test.com",
                    50000, "2024-01-01", "Italian", 5)
        waiter = Waiter(2, "Test Waiter", "+222222222", "waiter@test.com",
                        30000, "2024-01-01", "Main Hall")

        # Тест найма сотрудников
        emp_management.hire_employee(chef)
        emp_management.hire_employee(waiter)
        assert len(emp_management.employees) == 2

        # Тест поиска сотрудника по ID
        found_chef = emp_management.find_employee_by_id(1)
        assert found_chef == chef

        # Тест назначения смены
        emp_management.assign_shift(chef, "2024-01-20", "morning")
        assert chef.employee_id in emp_management.schedules

        print("✅ Employee management operations - PASSED")

    def test_customer_management_operations(self):
        """Тест операций управления клиентами"""
        customer_management = CustomerManagement()

        customer1 = Customer(1, "Alice", "+111111111", "alice@test.com")
        customer2 = Customer(2, "Bob", "+222222222", "bob@test.com")

        # Тест регистрации клиентов
        customer_management.register_customer(customer1)
        customer_management.register_customer(customer2)
        assert len(customer_management.customers) == 2

        # Тест поиска клиента по ID
        found_customer = customer_management.find_customer_by_id(1)
        assert found_customer == customer1

        # Тест поиска клиента по email
        found_by_email = customer_management.find_customer_by_email("bob@test.com")
        assert found_by_email == customer2

        # Тест получения топ клиентов
        customer1.total_spent = 1000.0
        customer2.total_spent = 500.0
        top_customers = customer_management.get_top_customers(1)
        assert len(top_customers) == 1
        assert top_customers[0] == customer1

        print("✅ Customer management operations - PASSED")

    def test_inventory_management_operations(self):
        """Тест операций управления инвентарем"""
        inventory_management = InventoryManagement()

        inventory_item = InventoryItem(1, "Flour", "Baking", 100, "kg", 20, 2.5)

        # Тест добавления товара в инвентарь
        inventory_management.add_inventory_item(inventory_item)
        assert len(inventory_management.inventory_items) == 1

        # Тест обновления уровня запасов
        inventory_management.update_stock_level(1, 80)
        assert inventory_item.quantity == 80

        # Тест поиска товара по ID
        found_item = inventory_management.find_item_by_id(1)
        assert found_item == inventory_item

        print("✅ Inventory management operations - PASSED")

    def test_reservation_management_operations(self):
        """Тест операций управления бронированиями"""
        reservation_management = ReservationManagement()

        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        table = Table(1, 4, "Window")
        reservation = Reservation(1, customer, table, "2024-12-31 19:00", 4)

        # Тест создания бронирования
        success = reservation_management.make_reservation(reservation)
        assert success == True
        assert len(reservation_management.reservations) == 1

        # Тест отмены бронирования
        reservation_management.cancel_reservation(1, "Change of plans")
        assert len(reservation_management.reservations) == 0

        print("✅ Reservation management operations - PASSED")

    def test_supplier_management_operations(self):
        """Тест операций управления поставщиками"""
        supplier_management = SupplierManagement()

        address = Address("Supplier St", "Supplier City", "54321")
        supplier = Supplier(1, "Test Supplier", "John Doe", "+999999999",
                            "john@supplier.com", address)

        # Тест добавления поставщика
        supplier_management.add_supplier(supplier)
        assert len(supplier_management.suppliers) == 1

        # Тест оценки поставщика
        supplier_management.evaluate_supplier(supplier, 4.5, "Great service")
        assert supplier.rating == 4.5

        print("✅ Supplier management operations - PASSED")


if __name__ == "__main__":
    test_instance = TestManagementModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")