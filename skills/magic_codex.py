class Spell:
    def __init__(self, name, damage, mana_cost, aoe=False):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.aoe = aoe

    def show_spell(self):
        print("==== SPELL ====")
        print(f"Name: {self.name}")
        print(f"Damage: {self.damage}")
        print(f"Mana Cost: {self.mana_cost}")
        print(f"AOE: {self.aoe}")