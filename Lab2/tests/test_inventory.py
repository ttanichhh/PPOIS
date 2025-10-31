#!/usr/bin/env python3
"""
Тесты для inventory модулей
"""

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from inventory.inventory import InventoryItem
from inventory.supplier import Supplier
from inventory.ingredient import Ingredient
from inventory.recipe import Recipe
from inventory.equipment import CookingEquipment
from inventory.kitchen import Kitchen

from support.address import Address
from core.employee import Chef
from exceptions.restaurant_exceptions import InventoryException


class TestInventoryModules:
    """Тесты инвентарных модулей"""

    def test_inventory_item_operations(self):
        """Тест операций с инвентарным товаром"""
        item = InventoryItem(1, "Flour", "Baking", 100, "kg", 20, 2.5)

        # Тест обновления количества
        item.update_quantity(80)
        assert item.quantity == 80

        # Тест проверки необходимости пополнения
        assert item.needs_restocking() == False

        item.update_quantity(15)
        assert item.needs_restocking() == True

        # Тест расчета общей стоимости
        total_value = item.get_total_value()
        assert total_value == 15 * 2.5

        print("✅ Inventory item operations - PASSED")

    def test_supplier_operations(self):
        """Тест операций с поставщиком"""
        address = Address("Supplier St", "Supplier City", "54321")
        supplier = Supplier(1, "Test Supplier", "John Doe", "+999999999",
                            "john@supplier.com", address)

        # Тест добавления поставляемого товара
        supplier.add_supplied_item("Flour")
        supplier.add_supplied_item("Sugar")
        assert "Flour" in supplier.supplied_items
        assert "Sugar" in supplier.supplied_items

        # Тест обновления рейтинга
        supplier.update_rating(4.7)
        assert supplier.rating == 4.7

        print("✅ Supplier operations - PASSED")

    def test_ingredient_operations(self):
        """Тест операций с ингредиентом"""
        ingredient = Ingredient(1, "Tomato", "piece", "Vegetable")

        # Тест добавления аллергена
        ingredient.add_allergen("Nightshade")
        assert "Nightshade" in ingredient.allergens

        # Тест установки пищевой информации
        ingredient.set_nutritional_info(22, 1.0, 5.0, 0.2)
        assert ingredient.nutritional_info["calories"] == 22
        assert ingredient.nutritional_info["protein"] == 1.0

        print("✅ Ingredient operations - PASSED")

    def test_recipe_operations(self):
        """Тест операций с рецептом"""
        recipe = Recipe(1, "Tomato Soup", "Cook tomatoes", 30)
        ingredient1 = Ingredient(1, "Tomato", "piece", "Vegetable")
        ingredient2 = Ingredient(2, "Onion", "piece", "Vegetable")

        # Тест добавления ингредиентов
        recipe.add_ingredient(ingredient1, 4.0)  # 4 tomatoes
        recipe.add_ingredient(ingredient2, 1.0)  # 1 onion
        assert len(recipe.ingredients) == 2

        print("✅ Recipe operations - PASSED")

    def test_equipment_operations(self):
        """Тест операций с оборудованием"""
        equipment = CookingEquipment(1, "Oven", "Baking", "operational")

        # Тест планирования обслуживания
        equipment.schedule_maintenance("2024-02-01")
        assert equipment.next_maintenance == "2024-02-01"

        # Тест отметки завершения обслуживания
        equipment.mark_maintenance_completed()
        assert equipment.status == "operational"
        assert equipment.last_maintenance is not None

        print("✅ Equipment operations - PASSED")

    def test_kitchen_operations(self):
        """Тест операций с кухней"""
        kitchen = Kitchen(1, "Test Kitchen", "Ground Floor")
        chef = Chef(1, "Test Chef", "+111111111", "chef@test.com",
                    50000, "2024-01-01", "Italian", 5)

        # Тест добавления оборудования
        kitchen.add_equipment("Oven")
        kitchen.add_equipment("Stove")
        assert "Oven" in kitchen.equipment
        assert "Stove" in kitchen.equipment

        # Тест открытия/закрытия кухни
        kitchen.close_kitchen()
        assert kitchen.is_open == False

        kitchen.open_kitchen()
        assert kitchen.is_open == True

        print("✅ Kitchen operations - PASSED")


if __name__ == "__main__":
    test_instance = TestInventoryModules()

    test_methods = [method for method in dir(test_instance)
                    if method.startswith('test_') and callable(getattr(test_instance, method))]

    for method_name in sorted(test_methods):
        try:
            method = getattr(test_instance, method_name)
            method()
            print(f"🎯 {method_name} - PASSED")
        except Exception as e:
            print(f"❌ {method_name} - FAILED: {str(e)}")