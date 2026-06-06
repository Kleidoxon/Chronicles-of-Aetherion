# equipment/weapon.py

from equipment.equipment_slot import EquipmentSlot


class Weapon:

    def __init__(
        self,
        name,
        rarity,
        attack_bonus
    ):

        self.name = name

        self.rarity = rarity

        self.attack_bonus = attack_bonus

        self.slot = EquipmentSlot.WEAPON