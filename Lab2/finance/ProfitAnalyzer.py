class ProfitAnalyzer:
    def __init__(self):
        self.revenue_data = []
        self.cost_data = []
        self.profit_margin = 0.0

    def calculate_profit(self, revenue, costs):
        if revenue < 0 or costs < 0:
            return "Revenue and costs must be positive"

        profit = revenue - costs
        margin = (profit / revenue) * 100 if revenue > 0 else 0

        self.revenue_data.append(revenue)
        self.cost_data.append(costs)
        self.profit_margin = margin

        performance = "Excellent" if margin > 20 else "Good" if margin > 10 else "Poor" if margin > 0 else "Loss"

        return f"Profit: ${profit:.2f}\nMargin: {margin:.1f}%\nPerformance: {performance}"

    def analyze_trends(self):
        if len(self.revenue_data) < 2:
            return "Need more data for trend analysis"

        avg_revenue = sum(self.revenue_data) / len(self.revenue_data)
        avg_costs = sum(self.cost_data) / len(self.cost_data)
        avg_margin = (avg_revenue - avg_costs) / avg_revenue * 100

        trend_report = f"Financial Trends Analysis\n"
        trend_report += f"Average Revenue: ${avg_revenue:.2f}\n"
        trend_report += f"Average Costs: ${avg_costs:.2f}\n"
        trend_report += f"Average Margin: {avg_margin:.1f}%\n"
        trend_report += f"Data Points: {len(self.revenue_data)} periods"
        return trend_report