class WorldWar:
    def __init__(self):
        self.active_wars = []

    def start_war(self, faction_a, faction_b):
        war = f"{faction_a} vs {faction_b}"

        self.active_wars.append(war)

        print(f"World War Started: {war}")