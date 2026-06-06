class PersistentWorld:
    def __init__(self):
        self.active_regions = []
        self.global_events = []

    def add_global_event(self, event):
        self.global_events.append(event)