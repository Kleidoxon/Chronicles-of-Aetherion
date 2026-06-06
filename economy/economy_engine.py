import random


class EconomyEngine:
    def __init__(self):
        self.market_state = "Stable"

    def update_market(self):
        states = [
            "Stable",
            "Boom",
            "Inflation",
            "Recession",
            "Wartime Economy"
        ]

        self.market_state = random.choice(states)

        print(f"Global Economy: {self.market_state}")