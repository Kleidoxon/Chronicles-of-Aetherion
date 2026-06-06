class WorldLog:
    def __init__(self):
        self.logs = []

    def add_log(self, event):
        self.logs.append(event)