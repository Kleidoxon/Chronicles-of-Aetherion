# player/attributes.py

class Attributes:

    def __init__(self):

        # Core Stats

        self.strength = 10

        self.dexterity = 10

        self.intelligence = 10

        self.vitality = 10

        self.wisdom = 10

        self.charisma = 10

        self.luck = 10

        # Advanced Stats

        self.faith = 0

        self.corruption = 0

        self.sanity = 100

        self.reputation = 0

    def show(self):

        print("\n=== ATTRIBUTES ===")

        print(f"Strength      : {self.strength}")
        print(f"Dexterity     : {self.dexterity}")
        print(f"Intelligence  : {self.intelligence}")
        print(f"Vitality      : {self.vitality}")
        print(f"Wisdom        : {self.wisdom}")
        print(f"Charisma      : {self.charisma}")
        print(f"Luck          : {self.luck}")

        print(f"Faith         : {self.faith}")
        print(f"Corruption    : {self.corruption}")
        print(f"Sanity        : {self.sanity}")
        print(f"Reputation    : {self.reputation}")