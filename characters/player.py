from classes.class_type import ClassType
from classes.class_registry import get_class_data


class Player:

    def __init__(self, name):

        self.name = name

        self.level = 1

        self.class_type = ClassType.WARRIOR

        self.load_class_stats()

    def load_class_stats(self):

        data = get_class_data(
            self.class_type
        )

        self.max_hp = data.hp
        self.max_mp = data.mp

        self.attack = data.attack
        self.defense = data.defense

        self.crit_rate = data.crit_rate

    def evolve(self, new_class):

        self.class_type = new_class

        self.load_class_stats()

    def display(self):

        print(
            f"{self.name} "
            f"| {self.class_type.value}"
        )

        print(
            f"HP:{self.max_hp} "
            f"MP:{self.max_mp}"
        )