# items/item_generator.py

import random

from equipment.weapon import Weapon

from items.loot_table import LootTable

from items.affix_generator import (
    AffixGenerator
)

from items.legendary_generator import (
    LegendaryGenerator
)

from items.item_rarity import (
    ItemRarity
)


class ItemGenerator:

    BASE_WEAPONS = [

        "Sword",

        "Axe",

        "Bow",

        "Dagger",

        "Hammer",

        "Revolver",

        "Rifle",

        "Spear",

        "Mace",

        "Staff",

        "Crossbow",

        "Scythe",

        "Flail",

        "Halberd",

        "Whip",

        "Katana",

        "Rapier",

        "Claymore",

        "Greatsword", 

        "Warhammer",

        "Longbow",

        "Shortbow",

        "Throwing Axe",

        "Throwing Knife",

        "Blunderbuss",

        "Musket",

        "Sniper Rifle",

        "Light Crossbow",

        "Heavy Crossbow",

        "Hand Cannon",

        "Energy Blade",

        "Plasma Rifle",

        "Laser Pistol",

        "Gravity Hammer",

        "Void Staff",

        "Arcane Wand",

        "Frost Axe",

        "Inferno Sword",

        "Storm Bow",

        "Shadow Dagger",

        "Radiant Mace",

        "Venom Spear",

        "Crystal Scythe",

        "Thunder Flail",

        "Solar Halberd",

        "Lunar Whip",

        "Phantom Katana",

        "Scepter of Light",

        "Scepter of Darkness",

        "Scepter of the Void",

        "Scepter of the Cosmos",

        "Scepter of the Ancients",

    ]

    @staticmethod
    def generate_weapon():

        rarity = LootTable.roll_rarity()

        if rarity.value >= (
            ItemRarity.LEGENDARY.value
        ):

            name = (
                LegendaryGenerator.generate()
            )

        else:

            base = random.choice(
                ItemGenerator.BASE_WEAPONS
            )

            name = (
                AffixGenerator.generate_name(
                    base
                )
            )

        attack_bonus = (
            rarity.value * 5
        )

        item_level = (
            rarity.value * 10
        )

        value = (
            rarity.value * 100
        )

        return Weapon(

            name=name,

            rarity=rarity.name,

            attack_bonus=attack_bonus,

            item_level=item_level,

            required_level=max(
            1,
            item_level // 2
        ),

        value=value
    )
