# combat/status_effects.py


class StatusEffect:

    def __init__(
        self,
        name,
        category,
        duration,
        damage_per_turn=0,
        healing_per_turn=0,
        percentage_modifier=0,
        percentage_maxhealth_damage_modifier=0,
        percentage_maxhealth_healing_modifier=0,
        attack_modifier=0,
        defense_modifier=0,

        strength_modifier=0,
        dexterity_modifier=0,
        magic_modifier=0,
        intelligence_modifier=0,
        resistance_modifier=0,

        speed_modifier=0,


        special_effect=None
    ):

        self.name = name
        self.category = category
        self.duration = duration

        self.damage_per_turn = damage_per_turn
        self.healing_per_turn = healing_per_turn
        self.percentage_modifier = percentage_modifier
        self.percentage_maxhealth_damage_modifier = percentage_maxhealth_damage_modifier
        self.percentage_maxhealth_healing_modifier = percentage_maxhealth_healing_modifier

        self.attack_modifier = attack_modifier
        self.defense_modifier = defense_modifier

        self.speed_modifier = speed_modifier
        self.intelligence_modifier = intelligence_modifier
        self.strength_modifier = attack_modifier
        self.magic_modifier = attack_modifier
        self.dexterity_modifier = speed_modifier

        self.special_effect = special_effect

    def tick(self):

        self.duration -= 1

    def expired(self):

        return self.duration <= 0

    def __str__(self):

        return (
            f"{self.name}"
            f" [{self.category}] "
            f"({self.duration} turns)"
        )

class StatusFactory:

    # =====================================
    # PHYSICAL
    # =====================================

    @staticmethod
    def Bleeding():
        return StatusEffect(
            "Bleeding",
            "Physical",
            4,
            percentage_maxhealth_damage_modifier=5
        )

    @staticmethod
    def BrokenBone():
        return StatusEffect(
            "Broken Bone",
            "Physical",
            8,
            speed_modifier=-15,
            attack_modifier=-15
        )

    @staticmethod
    def Crippled():
        return StatusEffect(
            "Crippled",
            "Physical",
            6,
            speed_modifier=-25,
            attack_modifier=-25
        )

    @staticmethod
    def PhysicalExhaustion():
        return StatusEffect(
            "Physical Exhaustion",
            "Physical",
            5,
            attack_modifier=-8,
            speed_modifier=-8,
            strength_modifier=-8
        )

    # =====================================
    # Mental
    # =====================================

    @staticmethod
    def fear():
    
     return StatusEffect(
        "Fear",
        "Mental",
        3,
        attack_modifier=-5,
        strength_modifier=-5
    )

    @staticmethod
    def madness():
     return StatusEffect(
        "Madness",
        "Mental",
        10,
        attack_modifier=15,
        defense_modifier=-10
    )

    @staticmethod
    def confusion():
     return StatusEffect(
        "Confusion",
        "Mental",
        3,
        attack_modifier=-10,
        defense_modifier=-10,
    )

    @staticmethod
    def panic():
     return StatusEffect(
        "Panic",
        "Mental",
        2,
        speed_modifier=-11
    )

    # =====================================
    # Divine
    # =====================================

    @staticmethod
    def blessed():
     return StatusEffect(
        "Blessed",
        "Divine",
        8,
        attack_modifier=5,
        defense_modifier=5
    )

    @staticmethod
    def cursed():
     return StatusEffect(
        "Cursed",
        "Divine",
        8,
        percentage_maxhealth_damage_modifier=5,
        attack_modifier=-5,
        defense_modifier=-5
    )

    @staticmethod
    def marked():
     return StatusEffect(
        "Marked",
        "Divine",
        5,
        defense_modifier=-3
    )

    @staticmethod
    def excommunicated():
        return StatusEffect(
        "Excommunicated",
        "Divine",
        20,
        attack_modifier=-10,
        defense_modifier=-10
    )

    @staticmethod
    def divine_protection():
       return StatusEffect(
        "Divine Protection",
        "Regeneration",
        30,
        percentage_maxhealth_healing_modifier=15,
        attack_modifier=10,
        defense_modifier=10
    )

    # =====================================
    # Cosmic
    # =====================================

    @staticmethod
    def void_corruption():
     return StatusEffect(
        "Void Corruption",
        "Cosmic",
        12,
        percentage_maxhealth_damage_modifier=10,
        attack_modifier=25
    )

    @staticmethod
    def reality_fracture():
     return StatusEffect(
        "Reality Fracture",
        "Cosmic",
        10,
        damage_per_turn=15,
        defense_modifier=-20
    )

    @staticmethod
    def temporal_instability():
     return StatusEffect(
        "Temporal Instability",
        "Cosmic",
        10,
        speed_modifier=-20,
        defense_modifier=-10
    )

    @staticmethod
    def dimensional_sickness():
     return StatusEffect(
        "Dimensional Sickness",
        "Cosmic",
        8,
        speed_modifier=-30,
        intelligence_modifier=-9,
        strength_modifier=-9,
        magic_modifier=-9,
    )

    @staticmethod
    def cosmic_blessing():
     return StatusEffect(
        "Cosmic Blessing",
        "Cosmic",
        15,
        attack_modifier=40,
        defense_modifier=40
    )

    @staticmethod
    def cosmic_curse():
     return StatusEffect(
        "Cosmic Curse",
        "Cosmic",
        15,
        attack_modifier=-40,
        defense_modifier=-40
    )

    # =====================================
    # Multiverse
    # =====================================

    @staticmethod
    def TimelineDrift():
        return StatusEffect(
            "Timeline Drift",
            "Multiverse",
            20,
            attack_modifier=-20,
            defense_modifier=-20,
            speed_modifier=-20,
        )

    @staticmethod
    def ParallelCollapse():
        return StatusEffect(
            "Parallel Collapse",
            "Multiverse",
            15,
            damage_per_turn=55,
            attack_modifier=-20,
            defense_modifier=-20,
            strength_modifier=-20,
            speed_modifier=-20,
    )        
