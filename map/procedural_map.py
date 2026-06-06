import random


class ProceduralMap:
    def generate_region(self):
        regions = [
            "Industrial Zone",
            "Mining Wasteland",
            "Forest Frontier",
            "Steam Harbor",
            "Ancient Ruins"
        ]

        return random.choice(regions)