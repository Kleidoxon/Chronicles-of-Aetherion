# player/player_class.py

class PlayerClass:

    def __init__(
        self,
        name,
        description
    ):

        self.name = name

        self.description = description

    def show(self):

        print(
            f"{self.name} - {self.description}"
        )


class DefaultClasses:

    @staticmethod
    def gunslinger():

        return PlayerClass(
            "Gunslinger",
            "Master of firearms and critical shots."
        )

    @staticmethod
    def warrior():

        return PlayerClass(
            "Warrior",
            "Frontline melee combat specialist."
        )

    @staticmethod
    def mage():

        return PlayerClass(
            "Mage",
            "Arcane spellcaster."
        )

    @staticmethod
    def rogue():

        return PlayerClass(
            "Rogue",
            "Stealth and assassination expert."
        )

    @staticmethod
    def engineer():

        return PlayerClass(
            "Engineer",
            "Builds machines and gadgets."
        )