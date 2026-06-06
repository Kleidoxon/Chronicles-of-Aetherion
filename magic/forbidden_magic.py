class ForbiddenSpell:
    def __init__(self, name, corruption):
        self.name = name
        self.corruption = corruption

    def cast(self):
        print(f"Casting forbidden spell: {self.name}") 