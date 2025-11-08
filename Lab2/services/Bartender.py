from entities.Order import Order


class Bartender:
    def __init__(self, bartender_id, name):
        self.bartender_id = bartender_id
        self.name = name
        self.specialty_drinks = []

    def prepare_drink(self, drink_name):
        drink_categories = {
            "cocktail": ["Measure ingredients", "Shake/stir", "Strain", "Garnish"],
            "beer": ["Select glass", "Pour at angle", "Top off"],
            "wine": ["Select bottle", "Uncork", "Pour taste", "Serve"]
        }

        category = "cocktail"
        for cat in drink_categories:
            if cat in drink_name.lower():
                category = cat
                break

        preparation = f"Preparing {drink_name} ({category})\n"
        for step in drink_categories[category]:
            preparation += f"🍸 {step}\n"
        preparation += "Drink ready for serving!"
        return preparation

    def manage_bar_stock(self):
        stock_items = ["Vodka", "Gin", "Rum", "Whiskey", "Wine", "Beer"]
        stock_levels = [80, 75, 85, 70, 90, 95]

        stock_report = f"Bar Stock - {self.name}\n"
        for item, level in zip(stock_items, stock_levels):
            status = "🟢" if level > 75 else "🟡" if level > 50 else "🔴"
            stock_report += f"{item}: {level}% {status}\n"
        stock_report += "Restock needed for low items"
        return stock_report