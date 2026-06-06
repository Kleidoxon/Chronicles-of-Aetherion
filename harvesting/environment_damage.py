class EnvironmentDamage:
    def __init__(self):
        self.pollution = 0
        self.forest_health = 100

    def mining_damage(self):
        self.pollution += 10
        self.forest_health -= 5

    def restore_environment(self):
        self.forest_health += 3