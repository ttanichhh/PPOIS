class Sommelier:
    def __init__(self, sommelier_id, name):
        self.sommelier_id = sommelier_id
        self.name = name
        self.wine_knowledge = ""

    def recommend_wine(self, dish):
        wine_pairings = {
            "steak": ["Cabernet Sauvignon", "Malbec", "Syrah"],
            "fish": ["Sauvignon Blanc", "Chardonnay", "Pinot Grigio"],
            "pasta": ["Chianti", "Pinot Noir", "Barbera"],
            "chicken": ["Chardonnay", "Pinot Noir", "Rosé"]
        }

        dish_type = "chicken"  # default
        for food_type in wine_pairings:
            if food_type in dish.name.lower():
                dish_type = food_type
                break

        recommendations = f"Wine Pairing for {dish.name}\n"
        recommendations += f"Recommended by: {self.name}\n"
        for i, wine in enumerate(wine_pairings[dish_type], 1):
            recommendations += f"{i}. {wine}\n"
        recommendations += "Perfect complement to your meal!"
        return recommendations

    def manage_wine_cellar(self):
        wine_categories = [
            "Red Wines: 45 bottles across 12 varieties",
            "White Wines: 35 bottles across 10 varieties",
            "Sparkling: 20 bottles across 5 varieties",
            "Dessert Wines: 15 bottles across 4 varieties"
        ]

        cellar_report = f"Wine Cellar Management\n"
        cellar_report += f"Sommelier: {self.name}\n"
        for category in wine_categories:
            cellar_report += f"• {category}\n"
        cellar_report += "Cellar well-stocked and organized"
        return cellar_report