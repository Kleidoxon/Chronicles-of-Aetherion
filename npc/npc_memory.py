class NPCMemory:
    def __init__(self):
        self.memories = []

    def remember(self, event):
        self.memories.append(event)

    def show_memories(self):
        for memory in self.memories:
            print(memory)