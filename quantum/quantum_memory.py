class QuantumMemory:
    def __init__(self):
        self.memories = []

    def store_memory(self, event):
        self.memories.append(event)