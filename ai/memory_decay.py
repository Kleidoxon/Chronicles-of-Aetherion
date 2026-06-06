class MemoryDecay:
    def decay_memory(self, npc_memory):
        if len(npc_memory.memories) > 10:
            npc_memory.memories.pop(0)