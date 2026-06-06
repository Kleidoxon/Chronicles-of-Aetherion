class City:
    def __init__(self, name):
        self.name = name
        self.population = 1000
        self.wealth = 5000
        self.pollution = 10
        self.stability = 75

    def collect_tax(self):
        tax = self.population * 2

        self.wealth += tax

        return tax