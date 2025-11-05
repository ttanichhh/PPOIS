import unittest
import sys
import os

# Добавляем пути для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from entities.customer import Customer
from entities.employee import Employee
from entities.menu_item import MenuItem
from entities.order import Order
from entities.reservation import Reservation
from entities.table import Table
from entities.payment import Payment
from entities.review import Review
from entities.invoice import Invoice
from entities.loyalty_member import LoyaltyMember

from management.restaurant_manager import RestaurantManager
from management.kitchen_manager import KitchenManager
from management.inventory_manager import InventoryManager
from management.hr_manager import HRManager
from management.finance_manager import FinanceManager
from management.order_manager import OrderManager
from management.menu_manager import MenuManager
from management.reservation_manager import ReservationManager
from management.quality_manager import QualityManager

from kitchen.chef import Chef
from kitchen.sous_chef import SousChef
from kitchen.line_cook import LineCook
from kitchen.pastry_chef import PastryChef
from kitchen.dish import Dish
from kitchen.recipe import Recipe
from kitchen.ingredient import Ingredient
from kitchen.kitchen_station import KitchenStation
from kitchen.food_preparation import FoodPreparation

from services.waiter import Waiter
from services.bartender import Bartender
from services.host import Host
from services.delivery_driver import DeliveryDriver
from services.customer_service import CustomerService
from services.cleaning_staff import CleaningStaff
from services.cashier import Cashier
from services.sommelier import Sommelier
from services.barista import Barista

from inventory.stock_item import StockItem
from inventory.supplier import Supplier
from inventory.inventory_tracker import InventoryTracker
from inventory.storage_unit import StorageUnit
from inventory.waste_tracker import WasteTracker
from inventory.order_processor import OrderProcessor

from finance.expense_tracker import ExpenseTracker
from finance.profit_analyzer import ProfitAnalyzer
from finance.tax_calculator import TaxCalculator
from finance.payroll_manager import PayrollManager
from finance.budget_planner import BudgetPlanner

from utils.date_utils import DateUtils
from utils.validation_utils import ValidationUtils
from utils.report_generator import ReportGenerator

from exceptions.restaurant_exceptions import RestaurantException
from exceptions.order_exceptions import OrderException
from exceptions.reservation_exceptions import ReservationException
from exceptions.payment_exceptions import PaymentException
from exceptions.inventory_exceptions import InventoryException
from exceptions.employee_exceptions import EmployeeException
from exceptions.customer_exceptions import CustomerException
from exceptions.kitchen_exceptions import KitchenException
from exceptions.finance_exceptions import FinanceException
from exceptions.menu_exceptions import MenuException
from exceptions.delivery_exceptions import DeliveryException
from exceptions.service_exceptions import ServiceException


class TestCustomer(unittest.TestCase):
    def test_customer_creation(self):
        customer = Customer("C001", "John Doe", "555-1234")
        self.assertEqual(customer.customer_id, "C001")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.phone, "555-1234")

    def test_loyalty_points(self):
        customer = Customer("C001", "John Doe", "555-1234")
        result = customer.add_loyalty_points(50)
        self.assertEqual(customer.loyalty_points, 50)
        self.assertIn("50", result)

    def test_customer_info(self):
        customer = Customer("C001", "John Doe", "555-1234")
        info = customer.get_customer_info()
        self.assertIn("John Doe", info)
        self.assertIn("555-1234", info)


class TestEmployee(unittest.TestCase):
    def test_employee_creation(self):
        employee = Employee("E001", "Alice Smith", "Manager")
        self.assertEqual(employee.employee_id, "E001")
        self.assertEqual(employee.name, "Alice Smith")
        self.assertEqual(employee.position, "Manager")

    def test_bonus_calculation(self):
        employee = Employee("E001", "Alice Smith", "Manager")
        employee.salary = 50000
        bonus = employee.calculate_bonus(1.5)
        self.assertEqual(bonus, 7500.0)

    def test_employee_details(self):
        employee = Employee("E001", "Alice Smith", "Manager")
        details = employee.get_employee_details()
        self.assertIn("Alice Smith", details)
        self.assertIn("Manager", details)


class TestMenuItem(unittest.TestCase):
    def test_menu_item_creation(self):
        item = MenuItem("I001", "Pizza", 12.99)
        self.assertEqual(item.item_id, "I001")
        self.assertEqual(item.name, "Pizza")
        self.assertEqual(item.price, 12.99)

    def test_discount_application(self):
        item = MenuItem("I001", "Pizza", 100.0)
        new_price = item.apply_discount(20)
        self.assertEqual(new_price, 80.0)

    def test_item_info(self):
        item = MenuItem("I001", "Pizza", 12.99)
        info = item.get_item_info()
        self.assertIn("Pizza", info)
        self.assertIn("12.99", info)


class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        self.assertEqual(order.order_id, "O001")
        self.assertEqual(order.customer, customer)

    def test_add_items_to_order(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item1 = MenuItem("I001", "Pizza", 12.99)
        item2 = MenuItem("I002", "Pasta", 10.99)

        order.add_item(item1)
        order.add_item(item2)

        self.assertEqual(len(order.items), 2)
        self.assertEqual(order.total_amount, 23.98)

    def test_calculate_total(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item1 = MenuItem("I001", "Pizza", 12.99)
        item2 = MenuItem("I002", "Pasta", 10.99)

        order.add_item(item1)
        order.add_item(item2)
        total = order.calculate_total()

        self.assertEqual(total, 23.98)
        self.assertEqual(order.total_amount, 23.98)

    def test_order_summary(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item = MenuItem("I001", "Pizza", 12.99)
        order.add_item(item)

        summary = order.get_order_summary()
        self.assertIn("O001", summary)
        self.assertIn("12.99", summary)


class TestReservation(unittest.TestCase):
    def test_reservation_creation(self):
        customer = Customer("C001", "John", "555-1234")
        reservation = Reservation("R001", customer, "2024-01-15")
        self.assertEqual(reservation.reservation_id, "R001")
        self.assertEqual(reservation.customer, customer)
        self.assertEqual(reservation.date, "2024-01-15")

    def test_update_guests(self):
        customer = Customer("C001", "John", "555-1234")
        reservation = Reservation("R001", customer, "2024-01-15")
        reservation.update_guests(4)
        self.assertEqual(reservation.guests, 4)

    def test_reservation_info(self):
        customer = Customer("C001", "John", "555-1234")
        reservation = Reservation("R001", customer, "2024-01-15")
        info = reservation.get_reservation_info()
        self.assertIn("John", info)
        self.assertIn("2024-01-15", info)


class TestTable(unittest.TestCase):
    def test_table_creation(self):
        table = Table("T001", 4)
        self.assertEqual(table.table_id, "T001")
        self.assertEqual(table.capacity, 4)

    def test_table_occupancy(self):
        table = Table("T001", 4)
        table.occupy_table()
        self.assertTrue(table.is_occupied)
        table.free_table()
        self.assertFalse(table.is_occupied)

    def test_capacity_check(self):
        table = Table("T001", 4)
        self.assertTrue(table.can_accommodate(3))
        self.assertTrue(table.can_accommodate(4))
        self.assertFalse(table.can_accommodate(5))


class TestPayment(unittest.TestCase):
    def test_payment_creation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item = MenuItem("I001", "Pizza", 12.99)
        order.add_item(item)

        payment = Payment("P001", order)
        self.assertEqual(payment.payment_id, "P001")
        self.assertEqual(payment.order, order)
        self.assertEqual(payment.amount, 12.99)

    def test_payment_processing(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        payment = Payment("P001", order)

        result = payment.process_payment()
        self.assertTrue(result)
        self.assertEqual(payment.status, "completed")


class TestReview(unittest.TestCase):
    def test_review_creation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        review = Review("RV001", customer, order)

        self.assertEqual(review.review_id, "RV001")
        self.assertEqual(review.customer, customer)
        self.assertEqual(review.order, order)

    def test_rating_calculation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        review = Review("RV001", customer, order)
        review.rating = 4

        score = review.calculate_rating_score()
        self.assertEqual(score, 80)

    def test_review_summary(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        review = Review("RV001", customer, order)

        summary = review.get_review_summary()
        self.assertIn("John", summary)
        self.assertIn("5", summary)  # default rating is 5


class TestInvoice(unittest.TestCase):
    def test_invoice_creation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        invoice = Invoice("INV001", order)

        self.assertEqual(invoice.invoice_id, "INV001")
        self.assertEqual(invoice.order, order)

    def test_tax_calculation(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item = MenuItem("I001", "Pizza", 100.0)
        order.add_item(item)

        invoice = Invoice("INV001", order)
        tax = invoice.calculate_tax(0.1)

        self.assertEqual(tax, 10.0)
        self.assertEqual(invoice.tax_amount, 10.0)

    def test_total_amount(self):
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)
        item = MenuItem("I001", "Pizza", 100.0)
        order.add_item(item)

        invoice = Invoice("INV001", order)
        invoice.calculate_tax(0.1)
        total = invoice.get_total_amount()

        self.assertEqual(total, 110.0)


class TestLoyaltyMember(unittest.TestCase):
    def test_loyalty_member_creation(self):
        customer = Customer("C001", "John", "555-1234")
        member = LoyaltyMember(customer)

        self.assertEqual(member.customer, customer)
        self.assertEqual(member.tier, "bronze")

    def test_tier_upgrade(self):
        customer = Customer("C001", "John", "555-1234")
        member = LoyaltyMember(customer)

        member.points_balance = 600
        member.upgrade_tier()
        self.assertEqual(member.tier, "silver")

        member.points_balance = 1200
        member.upgrade_tier()
        self.assertEqual(member.tier, "gold")

    def test_member_info(self):
        customer = Customer("C001", "John", "555-1234")
        member = LoyaltyMember(customer)

        info = member.get_member_info()
        self.assertIn("John", info)
        self.assertIn("bronze", info)


class TestRestaurantManager(unittest.TestCase):
    def test_manager_creation(self):
        manager = RestaurantManager("M001", "Sarah Johnson")
        self.assertEqual(manager.manager_id, "M001")
        self.assertEqual(manager.name, "Sarah Johnson")

    def test_daily_report(self):
        manager = RestaurantManager("M001", "Sarah Johnson")
        report = manager.generate_daily_report("2024-01-15")
        self.assertIn("2024-01-15", report)

    def test_special_request_approval(self):
        manager = RestaurantManager("M001", "Sarah Johnson")
        result = manager.approve_special_request("VIP table")
        self.assertIn("VIP table", result)
        self.assertIn("approved", result)


class TestKitchenManager(unittest.TestCase):
    def test_kitchen_manager_creation(self):
        manager = KitchenManager("KM001", "Chef Mike")
        self.assertEqual(manager.manager_id, "KM001")
        self.assertEqual(manager.name, "Chef Mike")

    def test_performance_monitoring(self):
        manager = KitchenManager("KM001", "Chef Mike")
        result = manager.monitor_kitchen_performance()
        self.assertEqual(result, "Kitchen performance monitored")


class TestInventoryManager(unittest.TestCase):
    def test_inventory_manager_creation(self):
        manager = InventoryManager("IM001", "Inventory Bob")
        self.assertEqual(manager.manager_id, "IM001")
        self.assertEqual(manager.name, "Inventory Bob")

    def test_low_stock_check(self):
        manager = InventoryManager("IM001", "Inventory Bob")
        stock_item = StockItem("S001", "Flour", 5)  # quantity below reorder level
        manager.inventory_items.append(stock_item)

        low_stock = manager.check_low_stock()
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0].name, "Flour")


class TestHRManager(unittest.TestCase):
    def test_hr_manager_creation(self):
        manager = HRManager("HR001", "HR Helen")
        self.assertEqual(manager.manager_id, "HR001")
        self.assertEqual(manager.name, "HR Helen")

    def test_employee_hiring(self):
        manager = HRManager("HR001", "HR Helen")
        employee = Employee("E001", "John", "Waiter")

        result = manager.hire_employee(employee)
        self.assertIn("John", result)
        self.assertIn(employee, manager.employees)


class TestFinanceManager(unittest.TestCase):
    def test_finance_manager_creation(self):
        manager = FinanceManager("FM001", "Finance Frank")
        self.assertEqual(manager.manager_id, "FM001")
        self.assertEqual(manager.name, "Finance Frank")

    def test_financial_analysis(self):
        manager = FinanceManager("FM001", "Finance Frank")
        result = manager.analyze_financial_data()
        self.assertEqual(result, "Financial data analyzed")


class TestOrderManager(unittest.TestCase):
    def test_order_manager_creation(self):
        manager = OrderManager("OM001", "Order Olivia")
        self.assertEqual(manager.manager_id, "OM001")
        self.assertEqual(manager.name, "Order Olivia")

    def test_order_processing(self):
        manager = OrderManager("OM001", "Order Olivia")
        customer = Customer("C001", "John", "555-1234")
        order = Order("O001", customer)

        result = manager.process_order(order)
        self.assertIn("O001", result)
        self.assertEqual(order.status, "processing")


class TestMenuManager(unittest.TestCase):
    def test_menu_manager_creation(self):
        manager = MenuManager("MM001", "Menu Mary")
        self.assertEqual(manager.manager_id, "MM001")
        self.assertEqual(manager.name, "Menu Mary")

    def test_menu_item_addition(self):
        manager = MenuManager("MM001", "Menu Mary")
        item = MenuItem("I001", "Pizza", 12.99)

        result = manager.add_menu_item(item)
        self.assertIn("Pizza", result)
        self.assertIn(item, manager.menu_items)


class TestReservationManager(unittest.TestCase):
    def test_reservation_manager_creation(self):
        manager = ReservationManager("RM001", "Reservation Rick")
        self.assertEqual(manager.manager_id, "RM001")
        self.assertEqual(manager.name, "Reservation Rick")

    def test_availability_check(self):
        manager = ReservationManager("RM001", "Reservation Rick")
        result = manager.check_availability("2024-01-15", "19:00")
        self.assertIn("2024-01-15", result)
        self.assertIn("19:00", result)


class TestQualityManager(unittest.TestCase):
    def test_quality_manager_creation(self):
        manager = QualityManager("QM001", "Quality Quinn")
        self.assertEqual(manager.manager_id, "QM001")
        self.assertEqual(manager.name, "Quality Quinn")

    def test_quality_check(self):
        manager = QualityManager("QM001", "Quality Quinn")
        result = manager.conduct_quality_check()
        self.assertEqual(result, "Quality check conducted")


class TestChef(unittest.TestCase):
    def test_chef_creation(self):
        chef = Chef("CH001", "Master Chef")
        self.assertEqual(chef.chef_id, "CH001")
        self.assertEqual(chef.name, "Master Chef")

    def test_recipe_creation(self):
        chef = Chef("CH001", "Master Chef")
        result = chef.create_recipe("Secret Sauce")
        self.assertIn("Secret Sauce", result)
        self.assertEqual(len(chef.recipes), 1)


class TestSousChef(unittest.TestCase):
    def test_sous_chef_creation(self):
        sous_chef = SousChef("SC001", "Assistant Chef")
        self.assertEqual(sous_chef.chef_id, "SC001")
        self.assertEqual(sous_chef.name, "Assistant Chef")

    def test_station_supervision(self):
        sous_chef = SousChef("SC001", "Assistant Chef")
        result = sous_chef.supervise_station("Grill Station")
        self.assertIn("Grill Station", result)


class TestLineCook(unittest.TestCase):
    def test_line_cook_creation(self):
        cook = LineCook("LC001", "Grill Master")
        self.assertEqual(cook.cook_id, "LC001")
        self.assertEqual(cook.name, "Grill Master")

    def test_dish_preparation(self):
        cook = LineCook("LC001", "Grill Master")
        dish = Dish("D001", "Steak")
        result = cook.prepare_dish(dish)
        self.assertIn("Steak", result)


class TestPastryChef(unittest.TestCase):
    def test_pastry_chef_creation(self):
        pastry_chef = PastryChef("PC001", "Dessert Queen")
        self.assertEqual(pastry_chef.chef_id, "PC001")
        self.assertEqual(pastry_chef.name, "Dessert Queen")

    def test_dessert_creation(self):
        pastry_chef = PastryChef("PC001", "Dessert Queen")
        result = pastry_chef.create_dessert("Chocolate Cake")
        self.assertIn("Chocolate Cake", result)


class TestDish(unittest.TestCase):
    def test_dish_creation(self):
        dish = Dish("D001", "Lasagna")
        self.assertEqual(dish.dish_id, "D001")
        self.assertEqual(dish.name, "Lasagna")

    def test_prep_time_calculation(self):
        dish = Dish("D001", "Complex Dish")
        ingredient1 = Ingredient("Flour", 100)
        ingredient2 = Ingredient("Sugar", 50)

        dish.add_ingredient(ingredient1)
        dish.add_ingredient(ingredient2)

        prep_time = dish.calculate_prep_time()
        self.assertEqual(prep_time, 14)  # 2 ingredients * 2 + 10 = 14


class TestRecipe(unittest.TestCase):
    def test_recipe_creation(self):
        recipe = Recipe("Pasta", "Boil for 10 minutes")
        self.assertEqual(recipe.name, "Pasta")
        self.assertEqual(recipe.instructions, "Boil for 10 minutes")

    def test_ingredient_list(self):
        recipe = Recipe("Pasta", "Boil for 10 minutes")
        ingredient = Ingredient("Pasta", 200)
        recipe.add_ingredient(ingredient)

        ingredients = recipe.get_ingredient_list()
        self.assertIn("Pasta", ingredients)


class TestIngredient(unittest.TestCase):
    def test_ingredient_creation(self):
        ingredient = Ingredient("Flour", 500)
        self.assertEqual(ingredient.name, "Flour")
        self.assertEqual(ingredient.quantity, 500)

    def test_quality_check(self):
        ingredient = Ingredient("Flour", 500)
        ingredient.quality = "Excellent"
        result = ingredient.check_quality()
        self.assertIn("Excellent", result)


class TestKitchenStation(unittest.TestCase):
    def test_station_creation(self):
        station = KitchenStation("KS001", "Grill Station")
        self.assertEqual(station.station_id, "KS001")
        self.assertEqual(station.name, "Grill Station")

    def test_cook_assignment(self):
        station = KitchenStation("KS001", "Grill Station")
        cook = LineCook("LC001", "Grill Master")

        result = station.assign_cook(cook)
        self.assertIn("Grill Master", result)
        self.assertEqual(station.assigned_cook, cook)


class TestFoodPreparation(unittest.TestCase):
    def test_preparation_creation(self):
        prep = FoodPreparation("FP001")
        self.assertEqual(prep.prep_id, "FP001")

    def test_prep_step_addition(self):
        prep = FoodPreparation("FP001")
        prep.add_prep_step("Chop vegetables")
        self.assertIn("Chop vegetables", prep.prep_steps)


class TestWaiter(unittest.TestCase):
    def test_waiter_creation(self):
        waiter = Waiter("W001", "Service Sam")
        self.assertEqual(waiter.waiter_id, "W001")
        self.assertEqual(waiter.name, "Service Sam")

    def test_order_taking(self):
        waiter = Waiter("W001", "Service Sam")
        customer = Customer("C001", "John", "555-1234")
        item = MenuItem("I001", "Pizza", 12.99)

        order = waiter.take_order(customer, [item])
        self.assertEqual(order.customer, customer)
        self.assertIn(item, order.items)


class TestBartender(unittest.TestCase):
    def test_bartender_creation(self):
        bartender = Bartender("B001", "Cocktail Carl")
        self.assertEqual(bartender.bartender_id, "B001")
        self.assertEqual(bartender.name, "Cocktail Carl")

    def test_drink_preparation(self):
        bartender = Bartender("B001", "Cocktail Carl")
        result = bartender.prepare_drink("Mojito")
        self.assertIn("Mojito", result)


class TestHost(unittest.TestCase):
    def test_host_creation(self):
        host = Host("H001", "Welcome Wendy")
        self.assertEqual(host.host_id, "H001")
        self.assertEqual(host.name, "Welcome Wendy")

    def test_customer_greeting(self):
        host = Host("H001", "Welcome Wendy")
        customer = Customer("C001", "John", "555-1234")
        result = host.greet_customer(customer)
        self.assertIn("John", result)


class TestDeliveryDriver(unittest.TestCase):
    def test_driver_creation(self):
        driver = DeliveryDriver("DD001", "Fast Fred")
        self.assertEqual(driver.driver_id, "DD001")
        self.assertEqual(driver.name, "Fast Fred")

    def test_delivery_time_calculation(self):
        driver = DeliveryDriver("DD001", "Fast Fred")
        time = driver.calculate_delivery_time(5)  # 5 km
        self.assertEqual(time, 15)  # 5 * 3 = 15 minutes


class TestCustomerService(unittest.TestCase):
    def test_customer_service_creation(self):
        service = CustomerService("CS001", "Helpful Hannah")
        self.assertEqual(service.rep_id, "CS001")
        self.assertEqual(service.name, "Helpful Hannah")

    def test_complaint_handling(self):
        service = CustomerService("CS001", "Helpful Hannah")
        result = service.handle_complaint("Cold food")
        self.assertIn("Cold food", result)
        self.assertEqual(service.complaints_resolved, 1)


class TestCleaningStaff(unittest.TestCase):
    def test_cleaning_staff_creation(self):
        staff = CleaningStaff("CL001", "Clean Chris")
        self.assertEqual(staff.staff_id, "CL001")
        self.assertEqual(staff.name, "Clean Chris")

    def test_area_cleaning(self):
        staff = CleaningStaff("CL001", "Clean Chris")
        result = staff.clean_area("Kitchen")
        self.assertIn("Kitchen", result)



class TestSommelier(unittest.TestCase):
    def test_sommelier_creation(self):
        sommelier = Sommelier("SO001", "Wine Walter")
        self.assertEqual(sommelier.sommelier_id, "SO001")
        self.assertEqual(sommelier.name, "Wine Walter")

    def test_wine_recommendation(self):
        sommelier = Sommelier("SO001", "Wine Walter")
        dish = Dish("D001", "Steak")
        result = sommelier.recommend_wine(dish)
        self.assertIn("Steak", result)


class TestBarista(unittest.TestCase):
    def test_barista_creation(self):
        barista = Barista("BA001", "Brew Brian")
        self.assertEqual(barista.barista_id, "BA001")
        self.assertEqual(barista.name, "Brew Brian")

    def test_coffee_preparation(self):
        barista = Barista("BA001", "Brew Brian")
        result = barista.prepare_coffee("Espresso")
        self.assertIn("Espresso", result)


class TestStockItem(unittest.TestCase):
    def test_stock_item_creation(self):
        item = StockItem("S001", "Flour", 50)
        self.assertEqual(item.item_id, "S001")
        self.assertEqual(item.name, "Flour")
        self.assertEqual(item.quantity, 50)

    def test_restocking_needed(self):
        item = StockItem("S001", "Flour", 5)  # below reorder level
        self.assertTrue(item.needs_restocking())


class TestSupplier(unittest.TestCase):
    def test_supplier_creation(self):
        supplier = Supplier("SUP001", "Fresh Foods Inc.")
        self.assertEqual(supplier.supplier_id, "SUP001")
        self.assertEqual(supplier.name, "Fresh Foods Inc.")

    def test_order_placement(self):
        supplier = Supplier("SUP001", "Fresh Foods Inc.")
        result = supplier.place_order(["Flour", "Sugar"])
        self.assertIn("Fresh Foods Inc.", result)


class TestInventoryTracker(unittest.TestCase):
    def test_tracker_creation(self):
        tracker = InventoryTracker("IT001")
        self.assertEqual(tracker.tracker_id, "IT001")

    def test_low_stock_finding(self):
        tracker = InventoryTracker("IT001")
        item1 = StockItem("S001", "Flour", 5)  # low stock
        item2 = StockItem("S002", "Sugar", 20)  # sufficient stock

        tracker.add_stock_item(item1)
        tracker.add_stock_item(item2)

        low_stock = tracker.find_low_stock()
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0].name, "Flour")


class TestStorageUnit(unittest.TestCase):
    def test_storage_unit_creation(self):
        unit = StorageUnit("SU001", "Main Storage")
        self.assertEqual(unit.unit_id, "SU001")
        self.assertEqual(unit.location, "Main Storage")

    def test_item_addition(self):
        unit = StorageUnit("SU001", "Main Storage")
        item = StockItem("S001", "Flour", 50)

        result = unit.add_item(item)
        self.assertTrue(result)
        self.assertIn(item, unit.current_items)

    def test_utilization_calculation(self):
        unit = StorageUnit("SU001", "Main Storage")
        unit.capacity = 10

        for i in range(5):
            item = StockItem(f"S{i}", f"Item{i}", 10)
            unit.add_item(item)

        utilization = unit.get_utilization()
        self.assertEqual(utilization, 50.0)  # 5/10 * 100 = 50%


class TestWasteTracker(unittest.TestCase):
    def test_waste_tracker_creation(self):
        tracker = WasteTracker("WT001")
        self.assertEqual(tracker.tracker_id, "WT001")

    def test_waste_recording(self):
        tracker = WasteTracker("WT001")
        tracker.record_waste("Bread", 2.5)
        tracker.record_waste("Vegetables", 1.5)

        self.assertEqual(len(tracker.waste_records), 2)
        self.assertEqual(tracker.total_waste, 4.0)


class TestOrderProcessor(unittest.TestCase):
    def test_processor_creation(self):
        processor = OrderProcessor("OP001")
        self.assertEqual(processor.processor_id, "OP001")

    def test_supplier_order_processing(self):
        processor = OrderProcessor("OP001")
        supplier = Supplier("SUP001", "Fresh Foods")

        result = processor.process_supplier_order(supplier, ["Flour", "Sugar"])
        self.assertIn("Fresh Foods", result)


class TestExpenseTracker(unittest.TestCase):
    def test_expense_tracker_creation(self):
        tracker = ExpenseTracker()
        self.assertEqual(tracker.monthly_budget, 0.0)

    def test_expense_addition(self):
        tracker = ExpenseTracker()
        tracker.add_expense(100.0, "Food")
        tracker.add_expense(50.0, "Utilities")

        self.assertEqual(len(tracker.expenses), 2)
        self.assertEqual(tracker.get_total_expenses(), 150.0)


class TestProfitAnalyzer(unittest.TestCase):
    def test_profit_analyzer_creation(self):
        analyzer = ProfitAnalyzer()
        self.assertEqual(analyzer.profit_margin, 0.0)

    def test_profit_calculation(self):
        analyzer = ProfitAnalyzer()
        profit = analyzer.calculate_profit(1000, 700)
        self.assertEqual(profit, 300)


class TestTaxCalculator(unittest.TestCase):
    def test_tax_calculator_creation(self):
        calculator = TaxCalculator()
        self.assertEqual(calculator.tax_rate, 0.1)

    def test_tax_calculation(self):
        calculator = TaxCalculator()
        tax = calculator.calculate_tax(1000)
        self.assertEqual(tax, 100.0)


class TestPayrollManager(unittest.TestCase):
    def test_payroll_manager_creation(self):
        manager = PayrollManager()
        self.assertEqual(manager.pay_period, "")

    def test_salary_calculation(self):
        manager = PayrollManager()
        employee = Employee("E001", "John", "Manager")
        employee.salary = 5000

        salary = manager.calculate_salary(employee)
        self.assertEqual(salary, 5000)


class TestBudgetPlanner(unittest.TestCase):
    def test_budget_planner_creation(self):
        planner = BudgetPlanner()
        self.assertEqual(len(planner.budget_categories), 0)

    def test_budget_allocation(self):
        planner = BudgetPlanner()
        planner.allocate_budget("Marketing", 5000)
        planner.allocate_budget("Operations", 10000)

        self.assertEqual(planner.allocated_amounts["Marketing"], 5000)
        self.assertEqual(planner.allocated_amounts["Operations"], 10000)


class TestDateUtils(unittest.TestCase):
    def test_date_utils_creation(self):
        utils = DateUtils()
        self.assertEqual(utils.date_format, "%Y-%m-%d")


class TestValidationUtils(unittest.TestCase):
    def test_validation_utils_creation(self):
        utils = ValidationUtils()
        self.assertEqual(len(utils.validation_rules), 0)

    def test_email_validation(self):
        utils = ValidationUtils()
        self.assertTrue(utils.validate_email("test@example.com"))
        self.assertFalse(utils.validate_email("invalid-email"))

    def test_phone_validation(self):
        utils = ValidationUtils()
        self.assertTrue(utils.validate_phone("1234567890"))
        self.assertFalse(utils.validate_phone("123"))


class TestReportGenerator(unittest.TestCase):
    def test_report_generator_creation(self):
        generator = ReportGenerator()
        self.assertEqual(len(generator.report_templates), 0)

    def test_report_generation(self):
        generator = ReportGenerator()
        result = generator.generate_report([1, 2, 3], "Sales Template")
        self.assertIn("Sales Template", result)


class TestExceptions(unittest.TestCase):
    def test_exceptions_creation(self):
        # Test that all exception classes can be instantiated
        exceptions = [
            RestaurantException(),
            OrderException(),
            ReservationException(),
            PaymentException(),
            InventoryException(),
            EmployeeException(),
            CustomerException(),
            KitchenException(),
            FinanceException(),
            MenuException(),
            DeliveryException(),
            ServiceException()
        ]

        self.assertEqual(len(exceptions), 12)
        for exc in exceptions:
            self.assertIsInstance(exc, Exception)


class TestIntegration(unittest.TestCase):
    def test_complete_order_flow(self):
        # Create customer
        customer = Customer("C001", "John Doe", "555-1234")

        # Create menu items
        pizza = MenuItem("I001", "Pizza", 12.99)
        pasta = MenuItem("I002", "Pasta", 10.99)

        # Create order
        order = Order("O001", customer)
        order.add_item(pizza)
        order.add_item(pasta)
        order.calculate_total()

        # Create payment
        payment = Payment("P001", order)
        payment.process_payment()

