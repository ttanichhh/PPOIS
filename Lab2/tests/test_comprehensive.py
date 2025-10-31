import pytest
import sys
import os

# Добавляем пути для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.restaurant import Restaurant
from core.customer import Customer
from core.employee import Chef, Waiter, Manager
from core.menu import Menu, MenuItem, MenuCategory
from core.order import Order, OrderItem
from core.table import Table

from support.address import Address
from support.person import Person
from support.payment import Payment
from support.reservation import Reservation
from support.delivery import Delivery
from support.discount import Discount
from support.promotion import Promotion
from support.review import Review
from support.shift import Shift

from inventory.inventory import InventoryItem
from inventory.supplier import Supplier
from inventory.ingredient import Ingredient
from inventory.recipe import Recipe
from inventory.equipment import CookingEquipment
from inventory.kitchen import Kitchen

from management.restaurant_management import RestaurantManagement
from management.employee_management import EmployeeManagement
from management.customer_management import CustomerManagement
from management.inventory_management import InventoryManagement
from management.reservation_management import ReservationManagement
from management.supplier_management import SupplierManagement

from services.ordering_service import OrderingService
from services.kitchen_service import KitchenService
from services.delivery_service import DeliveryService
from services.reporting_service import ReportingService
from services.table_management_service import TableManagementService

from financial.payment import PaymentProcessor
from financial.expense import ExpenseTracker, Expense
from financial.revenue import RevenueManager, Revenue
from financial.tax import TaxCalculator, Tax
from financial.bill import BillGenerator, Bill
from financial.payroll import PayrollSystem, Payroll

from utils.validation import ValidationUtils
from utils.notification import NotificationService, Notification
from utils.loyalty import LoyaltyManager, Reward
from utils.report import ReportGenerator, Report
from utils.security import SecurityManager, UserAccount

from exceptions.restaurant_exceptions import (
    RestaurantException, OrderException, PaymentException, ReservationException,
    MenuException, EmployeeException, TableException, InventoryException,
    CustomerException, KitchenException, DeliveryException, DiscountException
)
from exceptions.restaurant_exceptions import ValidationException

class TestComprehensiveRestaurantSystem:
    """Комплексный тест всей системы ресторана"""

    def test_01_core_entities_creation(self):
        """Тест создания основных сущностей"""
        # Address
        address = Address("Main St 123", "New York", "10001")
        assert address.street == "Main St 123"
        assert address.city == "New York"

        # Person
        person = Person(1, "John Doe", "+123456789", "john@test.com")
        assert person.name == "John Doe"
        assert person.phone == "+123456789"

        # Customer
        customer = Customer(1, "Alice Smith", "+111111111", "alice@test.com")
        assert customer.customer_id == 1
        assert customer.loyalty_points == 0

        # Employee и наследники
        chef = Chef(1, "Gordon Ramsay", "+222222222", "gordon@restaurant.com",
                    50000, "2024-01-01", "French", 10)
        assert chef.position == "Chef"
        assert chef.specialty == "French"

        waiter = Waiter(2, "Anna Service", "+333333333", "anna@restaurant.com",
                        30000, "2024-01-01", "Section A")
        assert waiter.position == "Waiter"
        assert waiter.section == "Section A"

        # Restaurant
        restaurant = Restaurant(1, "Gourmet Paradise", address, "+123456789", "French")
        assert restaurant.name == "Gourmet Paradise"
        assert restaurant.cuisine_type == "French"

        print("✅ Core entities creation - PASSED")

    def test_02_menu_system(self):
        """Тест-системы меню"""
        # MenuItem
        menu_item = MenuItem(1, "Steak", "Grilled steak with herbs", 45.99,
                             "Main Course", 25, 650)
        assert menu_item.name == "Steak"
        assert menu_item.price == 45.99
        assert menu_item.is_available == True

        # MenuCategory
        category = MenuCategory(1, "Main Courses", "Hearty main dishes", 1)
        category.add_menu_item(menu_item)
        assert len(category.menu_items) == 1

        # Menu
        menu = Menu(1, "Dinner Menu", "Evening menu")
        menu.add_category(category)
        assert len(menu.categories) == 1

        print("✅ Menu system - PASSED")

    def test_03_order_system(self):
        """Тест-системы заказов"""
        customer = Customer(1, "John Doe", "+123456789", "john@test.com")
        table = Table(1, 4, "Window")
        menu_item = MenuItem(1, "Pasta", "Fresh pasta", 18.99, "Main Course", 15)

        # OrderItem
        order_item = OrderItem(menu_item, 2, "Extra cheese")
        assert order_item.quantity == 2
        assert order_item.price == 37.98

        # Order
        order = Order(1, customer, table)
        order.add_item(order_item)
        assert len(order.order_items) == 1
        assert order.total_amount == 37.98
        assert order.status == "pending"

        print("✅ Order system - PASSED")

    def test_04_payment_system(self):
        """Тест платежной системы"""
        customer = Customer(1, "John Doe", "+123456789", "john@test.com")
        order = Order(1, customer)
        order.total_amount = 100.0

        # Payment
        payment = Payment(1, order, 100.0, "credit_card")
        payment.process_payment()
        assert payment.status == "completed"
        assert payment.payment_time is not None

        # PaymentProcessor
        processor = PaymentProcessor()
        result = processor.process_payment_transaction(payment)
        assert result == True
        assert len(processor.processed_payments) == 1

        print("✅ Payment system - PASSED")


    def test_05_reservation_system(self):
        """Тест-систем бронирования"""
        customer = Customer(1, "John Doe", "+123456789", "john@test.com")
        table = Table(1, 4, "Window")

        # Reservation
        reservation = Reservation(1, customer, table, "2024-12-31 19:00", 4)
        assert reservation.guests_count == 4
        assert reservation.status == "confirmed"

        # ReservationManagement
        reservation_mgmt = ReservationManagement()
        reservation_success = reservation_mgmt.make_reservation(reservation)  # 🔹 ИСПРАВЛЕНО: переименовал success
        assert reservation_success == True
        assert len(reservation_mgmt.reservations) == 1

        print("✅ Reservation system - PASSED")

    def test_06_inventory_system(self):
        """Тест-системы инвентаря"""
        # InventoryItem
        inventory_item = InventoryItem(1, "Beef", "Meat", 50, "kg", 10, 25.0)
        assert inventory_item.name == "Beef"
        assert inventory_item.quantity == 50
        assert inventory_item.needs_restocking() == False

        # Supplier
        address = Address("Supplier St 1", "Chicago", "60001")
        supplier = Supplier(1, "Meat Suppliers", "Bob Smith", "+444444444",
                            "bob@meat.com", address)
        supplier.add_supplied_item("Beef")
        assert "Beef" in supplier.supplied_items

        # InventoryManagement
        inventory_mgmt = InventoryManagement()
        inventory_mgmt.add_inventory_item(inventory_item)
        assert len(inventory_mgmt.inventory_items) == 1

        print("✅ Inventory system - PASSED")

    def test_07_employee_management(self):
        """Тест управления сотрудниками"""
        # EmployeeManagement
        emp_mgmt = EmployeeManagement()

        chef = Chef(1, "Gordon Ramsay", "+222222222", "gordon@restaurant.com",
                    50000, "2024-01-01", "French", 10)
        waiter = Waiter(2, "Anna Service", "+333333333", "anna@restaurant.com",
                        30000, "2024-01-01", "Section A")

        emp_mgmt.hire_employee(chef)
        emp_mgmt.hire_employee(waiter)

        assert len(emp_mgmt.employees) == 2
        assert emp_mgmt.find_employee_by_id(1) == chef

        print("✅ Employee management - PASSED")

    def test_08_customer_management(self):
        """Тест управления клиентами"""
        # CustomerManagement
        customer_mgmt = CustomerManagement()

        customer1 = Customer(1, "Alice Smith", "+111111111", "alice@test.com")
        customer2 = Customer(2, "Bob Johnson", "+222222222", "bob@test.com")

        customer_mgmt.register_customer(customer1)
        customer_mgmt.register_customer(customer2)

        assert len(customer_mgmt.customers) == 2
        assert customer_mgmt.find_customer_by_id(1) == customer1

        # Loyalty program
        customer1.add_loyalty_points(100)
        assert customer1.loyalty_points == 100

        print("✅ Customer management - PASSED")

    def test_09_kitchen_operations(self):
        """Тест операций кухни"""
        # Kitchen
        kitchen = Kitchen(1, "Main Kitchen", "Ground Floor")

        chef = Chef(1, "Gordon Ramsay", "+222222222", "gordon@restaurant.com",
                    50000, "2024-01-01", "French", 10)
        kitchen.chefs.append(chef)

        # KitchenService
        kitchen_service = KitchenService(kitchen)

        customer = Customer(1, "John Doe", "+123456789", "john@test.com")
        menu_item = MenuItem(1, "Steak", "Grilled steak", 45.99, "Main Course", 25)
        order = Order(1, customer)
        order_item = OrderItem(menu_item, 1)
        order.add_item(order_item)

        kitchen_service.receive_order(order)
        assert len(kitchen_service.kitchen.current_orders) == 1

        print("✅ Kitchen operations - PASSED")

    def test_10_delivery_system(self):
        """Тест-системы доставки"""
        customer = Customer(1, "John Doe", "+123456789", "john@test.com")
        order = Order(1, customer)
        order.total_amount = 75.0

        address = Address("Home St 123", "New York", "10001")
        delivery = Delivery(1, order, address, "2024-01-20 19:00")

        assert delivery.delivery_id == 1
        assert delivery.order == order
        assert delivery.delivery_address == address

        # DeliveryService
        delivery_service = DeliveryService()

        # Test delivery fee calculation
        fee = delivery_service.calculate_delivery_fee(3.0, 25.0)
        assert fee == 5.0  # Base fee for short distance

        free_fee = delivery_service.calculate_delivery_fee(2.0, 35.0)
        assert free_fee == 0.0  # Free delivery for orders over $30

        print("✅ Delivery system - PASSED")

    def test_11_financial_system(self):
        """Тест финансовой системы"""
        # Expense tracking
        expense_tracker = ExpenseTracker()
        expense = Expense(1, "food", 500.0, "2024-01-20", "Weekly groceries")
        expense_tracker.add_expense(expense)
        assert len(expense_tracker.expenses) == 1

        # Revenue management
        revenue_mgmt = RevenueManager()
        revenue = Revenue(1, "dine_in", 1000.0, "2024-01-20")
        revenue_mgmt.record_revenue(revenue)
        assert len(revenue_mgmt.revenue_streams) == 1

        # Tax calculation
        tax_calculator = TaxCalculator()
        tax = Tax(1, "Sales Tax", 8.5, ["general"])
        tax_calculator.add_tax_rate(tax)

        tax_amount = tax_calculator.calculate_tax(100.0)
        assert tax_amount == 8.5

        print("✅ Financial system - PASSED")

    def test_12_validation_utils(self):
        """Тест утилит валидации"""
        # Valid cases
        assert ValidationUtils.validate_email("test@example.com") == True
        assert ValidationUtils.validate_phone("+1234567890") == True
        assert ValidationUtils.validate_date("2024-01-20") == True

        # Invalid cases
        with pytest.raises(ValidationException):
            ValidationUtils.validate_email("invalid-email")

        with pytest.raises(ValidationException):
            ValidationUtils.validate_phone("abc")

        # Positive number validation
        assert ValidationUtils.validate_positive_number(100.0, "Price") == True

        with pytest.raises(ValidationException):
            ValidationUtils.validate_positive_number(-50.0, "Price")

        print("✅ Validation utils - PASSED")

    def test_13_exception_handling(self):
        """Тест обработки исключений"""
        # Customer exceptions
        customer = Customer(1, "John Doe", "+123456789", "john@test.com")

        with pytest.raises(CustomerException, match="Points must be positive"):
            customer.add_loyalty_points(-10)

        with pytest.raises(CustomerException, match="Not enough loyalty points"):
            customer.use_loyalty_points(100)

        # Order exceptions
        order = Order(1, customer)
        unavailable_item = MenuItem(1, "Unavailable", "Test", 10.0, "Test", 10)
        unavailable_item.is_available = False
        order_item = OrderItem(unavailable_item, 1)

        with pytest.raises(OrderException, match="Menu item is not available"):
            order.add_item(order_item)

        print("✅ Exception handling - PASSED")

    def test_14_integration_scenario(self):
        """Комплексный интеграционный сценарий"""
        # 1. Создаем ресторан
        address = Address("Main St 123", "New York", "10001")
        restaurant = Restaurant(1, "Integration Test Restaurant", address,
                                "+123456789", "International")

        # 2. Добавляем сотрудников
        chef = Chef(1, "Integration Chef", "+111111111", "chef@test.com",
                    45000, "2024-01-01", "Fusion", 8)
        waiter = Waiter(2, "Integration Waiter", "+222222222", "waiter@test.com",
                        28000, "2024-01-01", "Main Hall")

        restaurant.add_employee(chef)
        restaurant.add_employee(waiter)

        # 3. Создаем меню
        menu_item1 = MenuItem(1, "Integration Dish", "Test dish", 25.99,
                              "Main Course", 20)
        menu_item2 = MenuItem(2, "Integration Dessert", "Test dessert", 12.99,
                              "Dessert", 10)

        # 4. Регистрируем клиента
        customer = Customer(1, "Integration Customer", "+333333333",
                            "customer@test.com")
        restaurant.add_customer(customer)

        # 5. Создаем заказ
        order = Order(1, customer)
        order_item1 = OrderItem(menu_item1, 2)
        order_item2 = OrderItem(menu_item2, 1)

        order.add_item(order_item1)
        order.add_item(order_item2)
        restaurant.orders.append(order)

        # 6. Обрабатываем платеж
        payment = Payment(1, order, order.calculate_total(), "credit_card")
        payment.process_payment()

        # 7. Проверяем результаты
        assert len(restaurant.employees) == 2
        assert len(restaurant.customers) == 1
        assert len(restaurant.orders) == 1
        assert order.calculate_total() == (25.99 * 2 + 12.99)
        assert payment.status == "completed"

        print("✅ Integration scenario - PASSED")

    def test_15_business_workflow(self):
        """Тест полного бизнес потока"""
        # Restaurant Management
        address = Address("Business St 1", "New York", "10001")
        restaurant = Restaurant(1, "Business Test", address, "+123456789", "Italian")
        restaurant_mgmt = RestaurantManagement(restaurant)

        # Open restaurant
        restaurant_mgmt.open_restaurant()
        assert restaurant.is_open == True

        # Add tables
        table1 = Table(1, 2, "Window")
        table2 = Table(2, 4, "Center")
        restaurant.add_table(table1)
        restaurant.add_table(table2)

        # Customer makes reservation
        customer = Customer(1, "Business Customer", "+111111111", "business@test.com")
        reservation = Reservation(1, customer, table1, "2024-12-31 19:00", 2)

        reservation_mgmt = ReservationManagement()
        reservation_mgmt.make_reservation(reservation)

        # Customer arrives and orders
        menu_item = MenuItem(1, "Business Pizza", "Special pizza", 22.99, "Main", 15)
        order = Order(1, customer, table1)
        order_item = OrderItem(menu_item, 1)
        order.add_item(order_item)

        restaurant_mgmt.add_order(order)

        # Process payment
        payment = Payment(1, order, order.total_amount, "cash")
        payment.process_payment()
        restaurant_mgmt.complete_order(order, payment)

        # Verify business results
        assert restaurant_mgmt.daily_revenue == order.total_amount
        assert restaurant_mgmt.daily_customers == 1
        table1.occupy_table()
        assert table1.is_occupied == True

        print("✅ Business workflow - PASSED")


def run_comprehensive_test():
    """Запуск комплексного теста"""
    print("🚀 ЗАПУСК КОМПЛЕКСНОГО ТЕСТА СИСТЕМЫ РЕСТОРАНА")
    print("=" * 60)

    test_instance = TestComprehensiveRestaurantSystem()

    # Запускаем все тестовые методы
    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    passed = 0
    failed = 0

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
            passed += 1
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")
            failed += 1

    print("=" * 60)
    print(f"📊 ИТОГ: {passed} пройдено, {failed} не пройдено")

    if failed == 0:
        print("🎉 ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    else:
        print(f"⚠️  {failed} тестов не пройдено")

    return failed == 0


if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)