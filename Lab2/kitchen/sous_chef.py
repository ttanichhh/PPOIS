from kitchen.chef import Chef


class SousChef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.responsibilities = ""

    def supervise_station(self, station):
        return f"Supervising {station}"

    def assist_head_chef(self):
        return "Assisting head chef"