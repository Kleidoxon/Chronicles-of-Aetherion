import random


class SimpleMarket:
    def __init__(self):
        self.iron_price = 100

    def update(self):
        change = random.randint(-10, 10)

        self.iron_price += change

        print(f"Iron Price: {self.iron_price}")