class NavalFleet:
    def __init__(self, name, ships):
        self.name = name
        self.ships = ships

    def attack(self, enemy_fleet):
        print(f"{self.name} attacks {enemy_fleet.name}")