# items/loot_table.py

import random

from items.item_rarity import ItemRarity


class LootTable:

    @staticmethod
    def roll_rarity():

        roll = random.randint(
            1,
            1000
        )

        if roll <= 300:

            return ItemRarity.COMMON

        elif roll <= 550:

            return ItemRarity.UNCOMMON

        elif roll <= 750:

            return ItemRarity.RARE

        elif roll <= 900:

            return ItemRarity.EPIC

        elif roll <= 970:

            return ItemRarity.LEGENDARY

        elif roll <= 990:

            return ItemRarity.MYTHIC

        elif roll <= 997:

            return ItemRarity.DIVINE

        elif roll <= 999:

            return ItemRarity.COSMIC

        else:

            return ItemRarity.GODLIKE  