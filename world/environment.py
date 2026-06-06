class Environment:
    def __init__(self):
        self.forest_health = 100
        self.ocean_health = 100

    def mine(self):
        self.forest_health -= 5

    def restore(self):
        self.forest_health += 2