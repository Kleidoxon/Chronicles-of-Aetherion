import random


class GlobalMarket:
    def __init__(self):
        self.market_state = "Stable"

    def update_market(self):
        states = [
            "Boom",
            "Stable",
            "Recession",
            "Industrial Expansion",
            "Trade Collapse"
        ]

        self.market_state = random.choice(states)

        print(f"Global Market State: {self.market_state}")