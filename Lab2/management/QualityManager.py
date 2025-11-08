class QualityManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.quality_standards = ""
        self.inspection_schedule = ""

    def conduct_quality_check(self):
        check_points = [
            "Food temperature and freshness",
            "Table cleanliness and setup",
            "Staff hygiene and uniform",
            "Restroom cleanliness",
            "Kitchen sanitation"
        ]

        results = []
        for point in check_points:
            score = 95 if "cleanliness" in point.lower() else 92
            results.append(f"{point}: {score}%")

        report = f"Quality Inspection - {self.name}\n"
        for result in results:
            report += f"✓ {result}\n"
        report += "Overall: PASS"
        return report

    def generate_quality_report(self):
        metrics = {
            "Customer Satisfaction": "94%",
            "Food Quality": "96%",
            "Service Speed": "89%",
            "Cleanliness": "98%",
            "Staff Performance": "92%"
        }

        report = f"Quality Metrics Report\n"
        report += f"Manager: {self.name}\n"
        for metric, score in metrics.items():
            report += f"{metric}: {score}\n"
        report += "Target: All metrics above 85%"
        return report