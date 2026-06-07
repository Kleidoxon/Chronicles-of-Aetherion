# classes/character_class.py


class CharacterClass:

    def __init__(

        self,

        class_name,

        strength_bonus=0,

        dexterity_bonus=0,

        intelligence_bonus=0,

        vitality_bonus=0,

        wisdom_bonus=0,

        charisma_bonus=0,

        luck_bonus=0
    ):

        self.class_name = class_name

        self.strength_bonus = strength_bonus

        self.dexterity_bonus = dexterity_bonus

        self.intelligence_bonus = intelligence_bonus

        self.vitality_bonus = vitality_bonus

        self.wisdom_bonus = wisdom_bonus

        self.charisma_bonus = charisma_bonus

        self.luck_bonus = luck_bonus