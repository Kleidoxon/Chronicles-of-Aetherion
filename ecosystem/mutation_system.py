import random


class MutationSystem:
    def random_mutation(self):
        mutations = [
            "Metallic Skin",
            "Ether Vision",
            "Steam Blood",
            "Wing Growth",
            "Tentacle Arms",
            "Enhanced Strength",
            "Regeneration",
            "Telepathy",
            "Camouflage",
            "Acidic Touch"
            
        ]

        return random.choice(mutations)