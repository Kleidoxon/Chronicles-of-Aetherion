# player/player_background.py

class PlayerBackground:

    def __init__(
        self,
        name,
        description
    ):

        self.name = name

        self.description = description


class DefaultBackgrounds:

    @staticmethod
    def orphan():

        return PlayerBackground(
            "Orphan",
            "Raised without parents."
        )

    @staticmethod
    def noble():

        return PlayerBackground(
            "Noble",
            "Born into wealth."
        )

    @staticmethod
    def soldier():

        return PlayerBackground(
            "Soldier",
            "Veteran of war."
        )

    @staticmethod
    def scholar():

        return PlayerBackground(
            "Scholar",
            "Educated intellectual."
        )

    @staticmethod
    def criminal():

        return PlayerBackground(
            "Criminal",
            "Experienced in underground life."
        )