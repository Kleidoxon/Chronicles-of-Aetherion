from enum import Enum


class ClassTier(Enum):
    BASE = "Base"
    ADVANCED = "Advanced"
    LEGENDARY = "Legendary"


class ClassType(Enum):

    # ===== BASE =====
    WARRIOR = "Warrior"
    ROGUE = "Rogue"
    RANGER = "Ranger"
    MAGE = "Mage"
    PRIEST = "Priest"
    MONK = "Monk"
    ENGINEER = "Engineer"

    # ===== ADVANCED =====
    KNIGHT = "Knight"
    BARBARIAN = "Barbarian"
    ASSASSIN = "Assassin"
    HUNTER = "Hunter"
    GUNSLINGER = "Gunslinger"
    WIZARD = "Wizard"
    NECROMANCER = "Necromancer"
    PALADIN = "Paladin"
    SHAMAN = "Shaman"
    DUELIST = "Duelist"
    ALCHEMIST = "Alchemist"

    # ===== LEGENDARY =====
    DEATH_KNIGHT = "Death Knight"
    DRAGON_KNIGHT = "Dragon Knight"
    VOIDWALKER = "Voidwalker"
    CHRONOMANCER = "Chronomancer"
    DIMENSIONAL_LORD = "Dimensional Lord"
    BLOOD_MAGE = "Blood Mage"
    RUNEMASTER = "Runemaster"
    SPIRIT_WALKER = "Spirit Walker"
    BOUNTY_HUNTER = "Bounty Hunter"
    WITCH_HUNTER = "Witch Hunter"