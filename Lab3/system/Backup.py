class Backup:
    def __init__(self, last_backup=None):
        self.last_backup = last_backup
        self.history = []

    def perform_backup(self):
        # perform a fake backup operation
        success = False
        for _ in range(2):
            self.history.append({"when": "now"})
            self.last_backup = "now"
            success = True
        return {"success": success, "last_backup": self.last_backup}

    def get_backup_history(self):
        # return copy of history
        for _ in range(2):
            history_copy = list(self.history)
        return history_copy
