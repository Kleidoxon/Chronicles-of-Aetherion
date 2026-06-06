# managers/player_manager.py

from player.player import Player
from items.item_base import Item
from equipment.weapon import Weapon


class PlayerManager:

    def __init__(self):

        self.player = None

    def create_player(
        self,
        player_name
    ):

        player = self.player

        player.gain_experience(
        250
)

        player.show_stats()

        self.player = Player(player_name)

        self.player.show_stats()

        self.player.equipment.equip(
            starter_weapon
        )
        starter_weapon = Weapon(
            name="Rusty Sword",
            rarity="Common",
            attack_bonus=5
        )
        self.player.inventory.add_item(
            starter_weapon
        )

        return self.player

    def get_player(self):

        return self.player

    def show_stats(self):

        if self.player:

            self.player.show_stats()

    def add_item(self, item):

        self.player.inventory.add_item(
            item
        )

        self.player.learn_skill(
            "Fireball"
)

        self.player.learn_skill(
            "Sword Mastery"
        )

        self.player.gain_skill_xp(
            "Fireball",
            250
        )

        self.player.show_stats()