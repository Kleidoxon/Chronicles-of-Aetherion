# items/affix_generator.py

import random


class AffixGenerator:

    PREFIXES = [

        "Ancient",

        "Savage",

        "Infernal",

        "Holy",

        "Frozen",

        "Void",

        "Celestial",

        "Quantum",

    ]

    SUFFIXES = [

        "of Doom",

        "of Kings",

        "of Eternity",

        "of Chaos",

        "of Shadows",

        "of Creation",

        "of Infinity"

    ]

    @staticmethod
    def generate_name(base_name):

        prefix = random.choice(
            AffixGenerator.PREFIXES
        )

        suffix = random.choice(
            AffixGenerator.SUFFIXES
        )

        return (
            f"{prefix} "
            f"{base_name} "
            f"{suffix}"
        )