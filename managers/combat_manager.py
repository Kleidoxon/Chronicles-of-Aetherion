# managers/combat_manager.py

from combat.basic_battle import Battle

from combat.advanced_battle import AdvancedBattle

from combat.status_manager import StatusManager

from combat.combo_system import ComboSystem

from skills.magic_mastery import MagicMastery

from skills.massive_skill_tree import MassiveSkillTree

from combat.status_effects import StatusFactory


class CombatManager:

    def __init__(self):

        self.basic_battle = Battle()

        self.advanced_battle = AdvancedBattle()

        self.status_manager = StatusManager()

        self.combo_system = ComboSystem()

        self.magic_system = MagicMastery()

        self.skill_tree = MassiveSkillTree()

    def player_attack(
        self,
        player,
        enemy
    ):

        self.basic_battle.player_attack(
            player,
            enemy
        )

    def enemy_attack(
        self,
        enemy,
        player
    ):

        self.basic_battle.enemy_attack(
            enemy,
            player
        )

    def apply_status(
        self,
        target,
        effect
    ):

        self.status_manager.apply_effect(
            target,
            effect
        )

    def update(self):

        self.status_manager.process_turn()

        print(
            "Combat System Updated"
        )