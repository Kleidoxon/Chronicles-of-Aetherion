class WorldDatabase:
    def __init__(self):
        self.world_events = []
        self.discovered_locations = []
        self.defeated_enemies = []

    def log_event(self, event):
        self.world_events.append(event)