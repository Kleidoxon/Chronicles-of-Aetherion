# combat/damage_calculator.py

import random

from combat.combat_rules import CombatRules


class DamageCalculator:

    @staticmethod
    def calculate_damage(
        attacker,
        defender
    ):

        attack = (
            attacker.combat.attack_power
        )

        defense = (
            defender.combat.defense
        )

        damage = (
            attack -
            (defense * 0.5)
        )

        damage = max(
            CombatRules.MIN_DAMAGE,
            int(damage)
        )

        crit_chance = min(
            attacker.combat.crit_chance,
            CombatRules.MAX_CRIT_CHANCE
        )

        if random.randint(1, 100) <= crit_chance:

            damage = int(
                damage *
                CombatRules.CRIT_MULTIPLIER
            )

            print("CRITICAL HIT!")

        return damage