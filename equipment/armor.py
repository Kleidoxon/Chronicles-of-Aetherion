# equipment/armor.py

from equipment.equipment_slot import EquipmentSlot


class Armor:

    def __init__(
        self,
        name,
        rarity,
        defense_bonus,
        slot=EquipmentSlot.CHEST    
    ):

        self.name = name

        self.rarity = rarity

        self.defense_bonus = defense_bonus

        self.slot = slot