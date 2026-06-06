# equipment/accessory.py

from equipment.equipment_slot import EquipmentSlot


class Accessory:

    def __init__(
        self,
        name,
        rarity,
        stat_bonus,
        slot=EquipmentSlot.RING
    ):

        self.name = name

        self.rarity = rarity

        self.stat_bonus = stat_bonus

        self.slot = slot