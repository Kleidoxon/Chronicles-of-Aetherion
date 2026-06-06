# player/player_reputation.py

class Reputation:

    def __init__(self):

        self.global_reputation = 0

        self.city_reputation = {}

        self.faction_reputation = {}

    def modify_global(
        self,
        amount
    ):

        self.global_reputation += amount

    def modify_city(
        self,
        city,
        amount
    ):

        self.city_reputation.setdefault(
            city,
            0
        )

        self.city_reputation[city] += amount

    def modify_faction(
        self,
        faction,
        amount
    ):

        self.faction_reputation.setdefault(
            faction,
            0
        )

        self.faction_reputation[faction] += amount