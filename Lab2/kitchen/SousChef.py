from kitchen.Chef import Chef


class SousChef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.responsibilities = ""

    def supervise_station(self, station):
        stations = {
            "grill": ["Temperature control", "Meat preparation", "Timing management"],
            "saute": ["Sauce preparation", "Vegetable cooking", "Pan management"],
            "pastry": ["Dough preparation", "Baking control", "Decoration"]
        }

        if station.lower() not in stations:
            return f"Unknown station: {station}"

        supervision_report = f"Supervising {station.upper()} station\n"
        for task in stations[station.lower()]:
            supervision_report += f"✓ Monitoring {task}\n"
        supervision_report += "All tasks proceeding normally"
        return supervision_report

    def assist_head_chef(self):
        assistance_tasks = [
            "Review daily specials preparation",
            "Coordinate ingredient inventory",
            "Monitor cooking timelines",
            "Quality check finished dishes",
            "Train junior staff members"
        ]

        assistance_plan = f"Assistance plan for Head Chef\n"
        for task in assistance_tasks:
            assistance_plan += f"• {task}\n"
        assistance_plan += "Status: Ready to assist"
        return assistance_plan