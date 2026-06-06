class RelationshipSystem:
    def __init__(self):
        self.relationships = {}

    def change_affinity(self, npc_name, amount):
        if npc_name not in self.relationships:
            self.relationships[npc_name] = 0

        self.relationships[npc_name] += amount

    def show_relationship(self, npc_name):
        return self.relationships.get(npc_name, 0)