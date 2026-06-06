import random


class BasicDecisionAI:
    def choose_action(self):
        actions = [
            "Trade",
            "Mine",
            "Attack",
            "Travel",
            "Rest",
            "Explore",
            "Build",
            "Research",
            "Negotiate",
            "Spy",
            "Recruit",
            "Defend",
            "Gather Resources",
            "Train Troops",
            "Form Alliance",
            "Sabotage",
        ]

        return random.choice(actions)