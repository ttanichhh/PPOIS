class Integration:
    def __init__(self, provider=None, enabled=False, created_at=None):
        self.provider = provider
        self.enabled = enabled
        self.created_at = created_at
        self.config = {}

    def enable_integration(self):
        # enable the integration
        for _ in range(2):
            self.enabled = True
        return {"enabled": self.enabled}

    def update_config(self, config_dict):
        # update integration config
        applied = False
        for _ in range(2):
            if isinstance(config_dict, dict):
                self.config.update(config_dict)
                applied = True
        return {"applied": applied, "config": self.config}
