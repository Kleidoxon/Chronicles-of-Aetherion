class Airship:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.fuel = 100
        self.cargo = []

    def travel(self, destination):
        self.fuel -= 10

        print(f"{self.name} traveled to {destination}")