"""
Тесты для core модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Chef, Waiter, Manager
from core.menu import Menu, MenuItem, MenuCategory
from core.order import Order, OrderItem
from core.table import Table
from support.address import Address
from exceptions.restaurant_exceptions import CustomerException, OrderException, EmployeeException


class TestCoreModules:
    """Тесты основных модулей core"""

    def test_customer_loyalty_operations(self):
        """Тест операций с лояльностью клиента"""
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")

        # Тест добавления баллов
        customer.add_loyalty_points(50)
        assert customer.loyalty_points == 50

        # Тест использования баллов
        customer.use_loyalty_points(30)
        assert customer.loyalty_points == 20

        # Тест исключения при недостатке баллов
        try:
            customer.use_loyalty_points(30)
            assert False, "Should have raised CustomerException"
        except CustomerException:
            pass

        # Тест исключения при отрицательных баллах
        try:
            customer.add_loyalty_points(-10)
            assert False, "Should have raised CustomerException"
        except CustomerException:
            pass

        print("✅ Customer loyalty operations - PASSED")

    def test_employee_functionality(self):
        """Тест функциональности сотрудников"""
        # Тест шефа
        chef = Chef(1, "Test Chef", "+111111111", "chef@test.com",
                    50000, "2024-01-01", "Italian", 5)
        assert chef.position == "Chef"
        assert chef.specialty == "Italian"

        # Тест добавления сертификации
        chef.add_certification("Food Safety")
        assert "Food Safety" in chef.certifications

        # Тест официанта
        waiter = Waiter(2, "Test Waiter", "+222222222", "waiter@test.com",
                        30000, "2024-01-01", "Main Hall")
        waiter.add_tip(10.0)
        assert waiter.tips_collected == 10.0

        print("✅ Employee functionality - PASSED")

    def test_menu_operations(self):
        """Тест операций с меню"""
        # Создание элемента меню
        menu_item = MenuItem(1, "Test Pizza", "Delicious pizza", 15.99,
                             "Main Course", 20, 800)

        # Тест обновления цены
        menu_item.update_price(17.99)
        assert menu_item.price == 17.99

        # Тест добавления аллергена
        menu_item.add_allergen("Gluten")
        menu_item.add_allergen("Dairy")
        assert "Gluten" in menu_item.allergens
        assert "Dairy" in menu_item.allergens

        # Тест увеличения популярности
        menu_item.increment_popularity()
        assert menu_item.popularity_score == 1

        print("✅ Menu operations - PASSED")

    def test_order_operations(self):
        """Тест операций с заказами"""
        customer = Customer(1, "Test Customer", "+123456789", "test@test.com")
        order = Order(1, customer)

        menu_item1 = MenuItem(1, "Burger", "Tasty burger", 12.99, "Main", 15)
        menu_item2 = MenuItem(2, "Fries", "Crispy fries", 4.99, "Side", 5)

        # Добавление элементов в заказ
        order_item1 = OrderItem(menu_item1, 2)
        order_item2 = OrderItem(menu_item2, 1)

        order.add_item(order_item1)
        order.add_item(order_item2)

        # Проверка расчета общей суммы
        expected_total = (12.99 * 2) + 4.99
        assert order.calculate_total() == expected_total
        assert order.total_amount == expected_total

        # Тест добавления чаевых
        order.add_tip(5.0)
        assert order.tip_amount == 5.0

        # Тест отметки как обслуженного
        order.mark_as_served()
        assert order.status == "served"

        print("✅ Order operations - PASSED")

    def test_table_operations(self):
        """Тест операций со столами"""
        table = Table(1, 4, "Window")

        # Тест занятия стола
        table.occupy_table()
        assert table.is_occupied == True

        # Тест освобождения стола
        table.free_table()
        assert table.is_occupied == False
        assert table.cleanliness_status == "needs_cleaning"

        # Тест отметки как чистого
        table.mark_cleaned()
        assert table.cleanliness_status == "clean"

        print("✅ Table operations - PASSED")


if __name__ == "__main__":
    test_instance = TestCoreModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")