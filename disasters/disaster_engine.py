import random


class DisasterEngine:
    def trigger_disaster(self):
        disasters = [
            "Earthquake",
            "Volcanic Eruption",
            "Ether Storm",
            "Mega Flood",
            "Continental Drought"
        ]

        return random.choice(disasters)