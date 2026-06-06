import random


class DimensionalGenerator:
    def generate_dimension(self):
        dimensions = [
            "Clockwork Abyss",
            "Ether Void",
            "Mechanical Heaven",
            "Frozen Timeline",
            "Infinite Steam Realm"
        ]

        return random.choice(dimensions)