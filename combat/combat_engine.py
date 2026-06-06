import random


class CombatEngine:
    def attack(self, attacker, defender):
        damage = attacker.attack - defender.defense

        critical = random.randint(1, 100)

        if critical > 90:
            damage *= 2

        defender.health -= damage

        return damage