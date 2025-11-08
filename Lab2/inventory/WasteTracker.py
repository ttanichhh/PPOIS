class WasteTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.waste_records = []
        self.total_waste = 0.0

    def record_waste(self, item, amount):
        if amount <= 0:
            return "Waste amount must be positive"

        waste_value = amount * 2.5  # Simulated cost per unit
        self.waste_records.append((item, amount, waste_value))
        self.total_waste += waste_value

        monthly_waste = len([r for r in self.waste_records if "2024-01" in str(r)])
        trend = "📈 Increasing" if monthly_waste > 10 else "📉 Decreasing" if monthly_waste < 5 else "➡️ Stable"

        return f"Recorded waste: {amount} units of {item}\nCost: ${waste_value:.2f}\nMonthly trend: {trend}"

    def get_waste_report(self):
        if not self.waste_records:
            return "No waste records found"

        common_waste = {}
        for item, amount, value in self.waste_records:
            common_waste[item] = common_waste.get(item, 0) + amount

        top_waste = sorted(common_waste.items(), key=lambda x: x[1], reverse=True)[:3]

        report = f"Waste Report - Total Cost: ${self.total_waste:.2f}\n"
        report += "Top wasted items:\n"
        for item, amount in top_waste:
            report += f"• {item}: {amount} units\n"
        report += f"Total records: {len(self.waste_records)}"
        return report