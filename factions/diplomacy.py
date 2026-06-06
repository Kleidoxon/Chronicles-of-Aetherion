class Diplomacy:
    ALLIANCE_RELATION_BONUS = 25
    WAR_RELATION_PENALTY = -100

    def alliance(self, faction_a, faction_b):
        self._update_mutual_relation(faction_a, faction_b, self.ALLIANCE_RELATION_BONUS)
        print(f"{faction_a.name} formed alliance with {faction_b.name}")

    def declare_war(self, faction_a, faction_b):
        self._update_mutual_relation(faction_a, faction_b, self.WAR_RELATION_PENALTY)
        print(f"{faction_a.name} declared war on {faction_b.name}")

    def _update_mutual_relation(self, faction_a, faction_b, amount):
        faction_a.change_relation(faction_b.name, amount)
        faction_b.change_relation(faction_a.name, amount)
