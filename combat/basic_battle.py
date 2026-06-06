import random


class Battle:
    def player_attack(self, player, enemy):
        damage = player.attack + random.randint(1, 5)

        enemy.health -= damage

        print(f"You dealt {damage} damage")

    def enemy_attack(self, enemy, player):
        damage = enemy.attack + random.randint(1, 3)

        player.health -= damage

        print(f"Enemy dealt {damage} damage")