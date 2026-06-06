class Codex:
    def __init__(self):
        self.entries = {}

    def add_entry(self, category, data):
        if category not in self.entries:
            self.entries[category] = []

        self.entries[category].append(data)