# equipment/weapon.py

from equipment.equipment_base import (
    EquipmentBase
)

from equipment.equipment_slot import (
    EquipmentSlot
)


class Weapon(EquipmentBase):

    def __init__(
        self,
        name,
        rarity,
        attack_bonus,
        item_level=1,
        required_level=1,
        value=0
    ):

        super().__init__(

            name=name,

            rarity=rarity,

            slot=EquipmentSlot.WEAPON,

            item_level=item_level,

            required_level=required_level,

            value=value
        )

        self.attack_bonus = (
            attack_bonus
        )
