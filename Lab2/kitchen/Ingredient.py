from inventory.StockItem import StockItem


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.unit = ""
        self.quality = ""

    def check_quality(self):
        quality_indicators = {
            "color": "Vibrant" if self.quality == "fresh" else "Dull",
            "texture": "Firm" if self.quality == "fresh" else "Soft",
            "smell": "Pleasant" if self.quality == "fresh" else "Off",
            "appearance": "Good" if self.quality == "fresh" else "Poor"
        }

        quality_report = f"Quality check for {self.name}:\n"
        for indicator, status in quality_indicators.items():
            quality_report += f"{indicator.capitalize()}: {status}\n"

        overall = "✅ PASS" if self.quality == "fresh" else "❌ FAIL"
        quality_report += f"Overall: {overall}"
        return quality_report