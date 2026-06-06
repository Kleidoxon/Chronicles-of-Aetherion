# combat/combat_stats.py


class CombatStats:

    def __init__(self, player):

        self.player = player

    @property
    def attack_power(self):

        return (
            self.player.attributes.strength * 2
        
            +

            self.player.equipment.get_total_attack_bonus()
        )

    @property
    def magic_power(self):

        return (
            self.player.attributes.intelligence * 2
        )

    @property
    def defense(self):

        return (
            self.player.attributes.vitality
        
            +

            self.player.equipment.get_total_defense_bonus()
        )
            
    @property
    def speed(self):

        return (
            self.player.attributes.dexterity
        )

    @property
    def crit_chance(self):

        return (
            5 +
            self.player.attributes.luck
        )