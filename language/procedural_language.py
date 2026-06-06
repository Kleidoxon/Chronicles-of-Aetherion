import random


class ProceduralLanguage:
    def generate_word(self):
        syllables = [
            "aer",
            "vak",
            "tor",
            "zen",
            "kor",
            "lyth",
            "dra",
            "xen",
            "quar",
            "syl",
            "nix",
            "goth",
            "vel",
            "rax",
            "thar",
            "zyl",
            "kry",
            "mord",
            "vex",
            "laz",
            "fyr",
            "zark",
            "xal",
            "qir",
            "sor",
            "nex",
            "grel",
            "velk",
            "raxar",
            "tharx",
            "zylk",
            "kryx",
            "mordax",
            "vexar",
            "lazk",
            "fyrx",
            "zarkx",
            "xalr",
            "qirx",
            "sorx"    
        ]

        return random.choice(syllables) + random.choice(syllables)