# player/player_traits.py

class Trait:

    def __init__(
        self,
        name,
        description
    ):

        self.name = name

        self.description = description

    def __str__(self):

        return self.name


class DefaultTraits:

    BRAVE = Trait(
        "Brave",
        "Resists fear effects."
    )

    GENIUS = Trait(
        "Genius",
        "Learns faster."
    )

    LUCKY = Trait(
        "Lucky",
        "Improved loot chance."
    )

    GREEDY = Trait(
        "Greedy",
        "Earns more gold."
    )

    CURSED = Trait(
        "Cursed",
        "Attracts supernatural events."
    )

    QUICK = Trait(
        "Quick"
        "Improve dexterity"
    )    