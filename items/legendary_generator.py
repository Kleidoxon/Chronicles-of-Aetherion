# items/legendary_generator.py

import random


class LegendaryGenerator:

    LEGENDARY_NAMES = [

        "Aetherbreaker",

        "Voidfang",

        "Chronos Edge",

        "Starfall",

        "Soulreaper",

        "Worldshatter",

        "Eclipse",

        "Doombringer",

        "Phoenix Talon",

        "Dragonheart",

        "Shadowmourne",

        "Frostmourne",

        "Thunderfury",

        "Ashbringer",

        "Doomhammer",

        "Gorehowl",

        "Sulfuras",

        "Val'anyr",

        "Warglaives of Azzinoth",

        "Scepter of Sargeras",

        "Fang of the Leviathan",

        "Hammer of the Naaru",

        "Claw of the Frost Wyrm"

    ]

    @staticmethod
    def generate():

        return random.choice(
            LegendaryGenerator.LEGENDARY_NAMES
        )