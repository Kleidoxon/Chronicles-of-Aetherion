import random


class MutationSystem:
    def random_mutation(self):
        mutations = [
            "Metallic Skin",
            "Ether Vision",
            "Steam Blood",
            "Wing Growth"
        ]

        return random.choice(mutations)