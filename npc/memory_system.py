class MemorySystem:
    def __init__(self):
        self.memories = []

    def remember(self, event):
        self.memories.append(event)