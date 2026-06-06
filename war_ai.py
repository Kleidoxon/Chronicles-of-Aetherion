import random


class WarAI:
    def calculate_spoils(self, winner_power, loser_power):
        return int((winner_power / loser_power) * random.randint(1000, 5000))