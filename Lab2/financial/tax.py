class Tax:
    def __init__(self, tax_id: int, name: str, rate: float, applicable_categories: list):
        self.tax_id = tax_id
        self.name = name
        self.rate = rate
        self.applicable_categories = applicable_categories
        self.is_active = True
        self.effective_date = "2024-01-01"
        self.expiry_date = None


class TaxCalculator:
    def __init__(self):
        self.tax_rates = []
        self.tax_exempt_categories = ["essential_foods"]
        self.tax_records = []
        self.tax_filing_dates = []

    def add_tax_rate(self, tax: Tax):
        self.tax_rates.append(tax)

    def calculate_tax(self, amount: float, category: str = "general") -> float:
        total_tax = 0.0

        if category in self.tax_exempt_categories:
            return 0.0

        for tax in self.tax_rates:
            if tax.is_active and category in tax.applicable_categories:
                total_tax += amount * tax.rate / 100

        return total_tax

    def generate_tax_report(self, period: str) -> dict:
        taxable_transactions = []  # This would come from revenue records
        total_taxable_amount = sum(tx['amount'] for tx in taxable_transactions)
        total_tax_collected = sum(self.calculate_tax(tx['amount'], tx.get('category', 'general'))
                                  for tx in taxable_transactions)

        return {
            "period": period,
            "total_taxable_sales": total_taxable_amount,
            "total_tax_collected": total_tax_collected,
            "tax_breakdown": {tax.name: total_taxable_amount * tax.rate / 100 for tax in self.tax_rates}
        }