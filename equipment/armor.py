# equipment/armor.py

from equipment.equipment_base import (
    EquipmentBase
)


class Armor(EquipmentBase):

    def __init__(
        self,
        name,
        rarity,
        defense_bonus,
        slot,
        item_level=1,
        required_level=1,
        value=0
    ):

        super().__init__(

            name=name,

            rarity=rarity,

            slot=slot,

            item_level=item_level,

            required_level=required_level,

            value=value
        )

        self.defense_bonus = (
            defense_bonus
        )
