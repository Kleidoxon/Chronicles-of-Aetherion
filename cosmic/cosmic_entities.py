class CosmicEntity:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def awaken(self):
        print(f"Cosmic Entity {self.name} awakened")