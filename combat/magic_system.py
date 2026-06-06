class Spell:
    def __init__(self, name, damage, mana_cost, aoe=False):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.aoe = aoe