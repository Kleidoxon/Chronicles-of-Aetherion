import random


class HarvestingSystem:
    def fish(self):
        catches = [
            "Small Fish",
            "Sea Crab",
            "Rare Steam Tuna"
        ]

        return random.choice(catches)

    def mine(self):
        minerals = [
            "Iron Ore",
            "Coal",
            "Ether Crystal",
            "Mythril Shard"
            "Adamantium Fragment",
            "Voidstone",
            "Gold Ore",
            "Dark Matter",
            "Luminous Gem",
            "Ancient Relic",
            "Celestial Shard",
            "Steel Ore",
            "Clay",
            "Sand",
            "Gravel",
            "Salt",
            "Sulfur",
            "Phosphorus",
            "Quartz",
        ]

        return random.choice(minerals)