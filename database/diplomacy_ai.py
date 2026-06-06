import random


class DiplomacyAI:
    def decide_action(self):
        actions = [
            "Alliance",
            "Trade Pact",
            "Sanction",
            "Declare War",
            "Peace Negotiation"
        ]

        return random.choice(actions)