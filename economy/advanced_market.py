import random


class AdvancedMarket:
    def __init__(self):
        self.prices = {
            "Iron": 100,
            "Coal": 50,
            "Food": 25,
            "Ether Crystal": 500
        }

    def update_market(self):
        for item in self.prices:
            change = random.randint(-20, 20)
            self.prices[item] += change

        print("=== MARKET UPDATE ===")

        for item, price in self.prices.items():
            print(f"{item}: {price}")