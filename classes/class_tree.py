from classes.class_type import ClassType, ClassTier


# ==========================================
# CLASS EVOLUTION TREE
# ==========================================

CLASS_EVOLUTION = {

    # Warrior Path
    ClassType.WARRIOR: [
        ClassType.KNIGHT,
        ClassType.BARBARIAN,
    ],

    ClassType.KNIGHT: [
        ClassType.PALADIN,
        ClassType.DEATH_KNIGHT,
    ],

    ClassType.BARBARIAN: [
        ClassType.DRAGON_KNIGHT,
    ],

    # Rogue Path
    ClassType.ROGUE: [
        ClassType.ASSASSIN,
        ClassType.DUELIST,
    ],

    ClassType.ASSASSIN: [
        ClassType.BOUNTY_HUNTER,
        ClassType.WITCH_HUNTER,
    ],

    # Ranger Path
    ClassType.RANGER: [
        ClassType.HUNTER,
        ClassType.GUNSLINGER,
    ],

    # Mage Path
    ClassType.MAGE: [
        ClassType.WIZARD,
        ClassType.NECROMANCER,
    ],

    ClassType.WIZARD: [
        ClassType.CHRONOMANCER,
        ClassType.RUNEMASTER,
    ],

    ClassType.NECROMANCER: [
        ClassType.BLOOD_MAGE,
        ClassType.VOIDWALKER,
    ],

    ClassType.VOIDWALKER: [
        ClassType.DIMENSIONAL_LORD,
    ],

    # Priest Path
    ClassType.PRIEST: [
        ClassType.PALADIN,
        ClassType.SHAMAN,
    ],

    ClassType.SHAMAN: [
        ClassType.SPIRIT_WALKER,
    ],

    # Monk Path
    ClassType.MONK: [
        ClassType.DUELIST,
    ],

    # Engineer Path
    ClassType.ENGINEER: [
        ClassType.ALCHEMIST,
    ],
}


# ==========================================
# CLASS TIERS
# ==========================================

BASE_CLASSES = {
    ClassType.WARRIOR,
    ClassType.ROGUE,
    ClassType.RANGER,
    ClassType.MAGE,
    ClassType.PRIEST,
    ClassType.MONK,
    ClassType.ENGINEER,
}

ADVANCED_CLASSES = {
    ClassType.KNIGHT,
    ClassType.BARBARIAN,
    ClassType.ASSASSIN,
    ClassType.HUNTER,
    ClassType.GUNSLINGER,
    ClassType.WIZARD,
    ClassType.NECROMANCER,
    ClassType.PALADIN,
    ClassType.SHAMAN,
    ClassType.DUELIST,
    ClassType.ALCHEMIST,
}

LEGENDARY_CLASSES = {
    ClassType.DEATH_KNIGHT,
    ClassType.DRAGON_KNIGHT,
    ClassType.VOIDWALKER,
    ClassType.CHRONOMANCER,
    ClassType.DIMENSIONAL_LORD,
    ClassType.BLOOD_MAGE,
    ClassType.RUNEMASTER,
    ClassType.SPIRIT_WALKER,
    ClassType.BOUNTY_HUNTER,
    ClassType.WITCH_HUNTER,
}


# ==========================================
# UTILITIES
# ==========================================

def get_next_classes(class_type: ClassType):
    """
    Returns all possible evolutions for a class.
    """
    return CLASS_EVOLUTION.get(class_type, [])


def can_evolve(class_type: ClassType):
    """
    Returns True if class has evolutions.
    """
    return class_type in CLASS_EVOLUTION


def get_class_tier(class_type: ClassType):
    """
    Returns ClassTier.
    """

    if class_type in BASE_CLASSES:
        return ClassTier.BASE

    if class_type in ADVANCED_CLASSES:
        return ClassTier.ADVANCED

    return ClassTier.LEGENDARY


def is_base_class(class_type: ClassType):
    return class_type in BASE_CLASSES


def is_advanced_class(class_type: ClassType):
    return class_type in ADVANCED_CLASSES


def is_legendary_class(class_type: ClassType):
    return class_type in LEGENDARY_CLASSES


def get_all_classes():
    return list(ClassType)