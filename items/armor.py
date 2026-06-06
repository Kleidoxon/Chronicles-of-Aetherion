class Armor:
    def __init__(self, name, defense, durability, rarity="Common"):
        self.name = name
        self.defense = defense
        self.durability = durability
        self.rarity = rarity

    def take_damage(self, amount):
        self.durability -= amount

        if self.durability < 0:
            self.durability = 0

    def is_broken(self):
        return self.durability <= 0

    def show_stats(self):
        print("==== ARMOR ====")
        print(f"Name: {self.name}")
        print(f"Defense: {self.defense}")
        print(f"Durability: {self.durability}")
        print(f"Rarity: {self.rarity}")