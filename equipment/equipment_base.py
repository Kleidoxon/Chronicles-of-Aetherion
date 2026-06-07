# equipment/equipment_base.py

import uuid


class EquipmentBase:

    def __init__(
        self,
        name,
        rarity,
        slot,
        item_level=1,
        required_level=1,
        value=0,
        weight=1,
        durability=100,
        max_durability=100,
        description=""
    ):

        self.unique_id = str(
            uuid.uuid4()
        )

        self.name = name

        self.rarity = rarity

        self.slot = slot

        self.item_level = item_level

        self.required_level = required_level

        self.value = value

        self.weight = weight

        self.durability = durability

        self.max_durability = max_durability

        self.description = description

        self.affixes = []

    # ==========================
    # DURABILITY
    # ==========================

    def lose_durability(
        self,
        amount
    ):

        self.durability -= amount

        if self.durability < 0:

            self.durability = 0

    def repair(self):

        self.durability = (
            self.max_durability
        )

    # ==========================
    # AFFIXES
    # ==========================

    def add_affix(
        self,
        affix
    ):

        self.affixes.append(
            affix
        )

    # ==========================
    # DEBUG
    # ==========================

    def show(self):

        print(
            f"{self.name}"
        )

        print(
            f"Rarity: {self.rarity}"
        )

        print(
            f"Level: {self.item_level}"
        )

        print(
            f"Durability: "
            f"{self.durability}/"
            f"{self.max_durability}"
        )