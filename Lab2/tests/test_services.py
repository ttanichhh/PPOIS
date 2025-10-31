"""
Тесты для services модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from services.ordering_service import OrderingService
from services.kitchen_service import KitchenService
from services.delivery_service import DeliveryService
from services.table_management_service import TableManagementService

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Chef
from core.menu import MenuItem
from core.order import Order, OrderItem
from core.table import Table
from support.address import Address
from support.delivery import Delivery
from inventory.kitchen import Kitchen


class TestServicesModules:
    """Тесты сервисных модулей"""

    def test_ordering_service_operations(self):
        """Тест операций сервиса заказов"""
        menu_item1 = MenuItem(1, "Pizza", "Cheesy pizza", 15.99, "Main", 20)
        menu_item2 = MenuItem(2, "Salad", "Fresh salad", 8.99, "Starter", 10)

        ordering_service = OrderingService([menu_item1, menu_item2])
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        # Тест создания заказа
        order = ordering_service.create_order(customer, order_type="dine_in")
        assert order.customer == customer
        assert order.order_type == "dine_in"

        # Тест добавления элемента в заказ
        order_item = ordering_service.add_item_to_order(order, menu_item1, 2, "Extra cheese")
        assert order_item.quantity == 2
        assert len(order.order_items) == 1

        # Тест обновления количества
        ordering_service.update_item_quantity(order, order_item, 3)
        assert order_item.quantity == 3

        print("✅ Ordering service operations - PASSED")

    def test_kitchen_service_operations(self):
        """Тест операций сервиса кухни"""
        kitchen = Kitchen(1, "Test Kitchen", "Ground Floor")
        chef = Chef(1, "Test Chef", "+111111111", "chef@test.com",
                    50000, "2024-01-01", "Italian", 5)
        kitchen.chefs.append(chef)

        kitchen_service = KitchenService(kitchen)
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        menu_item = MenuItem(1, "Pasta", "Fresh pasta", 12.99, "Main", 15)

        # Создание заказа
        order = Order(1, customer)
        order_item = OrderItem(menu_item, 2)
        order.add_item(order_item)

        # Тест приема заказа
        kitchen_service.receive_order(order)
        assert len(kitchen_service.order_queue) == 1

        # Тест начала приготовления
        kitchen_service.start_preparation(order)
        assert order.status == "preparing"

        # Тест завершения приготовления
        kitchen_service.complete_preparation(order)
        assert order.status == "ready"

        print("✅ Kitchen service operations - PASSED")

    def test_delivery_service_operations(self):
        """Тест операций сервиса доставки"""
        delivery_service = DeliveryService()

        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)
        address = Address("Home St", "Test City", "12345")
        delivery = Delivery(1, order, address, "2024-01-20 19:00")

        # Тест расчета платы за доставку
        fee_short = delivery_service.calculate_delivery_fee(3.0, 25.0)
        assert fee_short == 5.0

        fee_long = delivery_service.calculate_delivery_fee(10.0, 25.0)
        assert fee_long == 7.5  # 5.0 + (10-5)*0.5

        fee_free = delivery_service.calculate_delivery_fee(3.0, 35.0)
        assert fee_free == 0.0

        # Тест проверки зоны доставки
        covered_address = Address("Test St", "New York", "10001")
        not_covered_address = Address("Test St", "Boston", "02101")

        assert delivery_service.is_delivery_zone_covered(covered_address) == True
        assert delivery_service.is_delivery_zone_covered(not_covered_address) == False

        print("✅ Delivery service operations - PASSED")

    def test_table_management_operations(self):
        """Тест операций управления столами"""
        table_service = TableManagementService()

        table1 = Table(1, 2, "Window")
        table2 = Table(2, 4, "Center")
        table3 = Table(3, 6, "Patio")
        tables = [table1, table2, table3]

        # Тест назначения стола группе
        assigned_table = table_service.assign_table_to_group(tables, 3)
        assert assigned_table == table2  # Стол на 4 человека

        # Тест утилизации столов
        utilization = table_service.get_table_utilization(tables, "2024-01-20")
        assert utilization["total_tables"] == 3
        assert utilization["occupied_tables"] == 0

        print("✅ Table management operations - PASSED")


if __name__ == "__main__":
    test_instance = TestServicesModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")