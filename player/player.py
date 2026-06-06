# player/player.py

from turtle import title

from player.attributes import Attributes
from player.player_resources import PlayerResources
from player.player_status import PlayerStatus
from inventory.inventory_system import Inventory
from combat.status_manager import StatusManager
from player.player_progression import PlayerProgression
from player.player_skills import PlayerSkills
from player.player_class import DefaultClasses
from player.player_background import DefaultBackgrounds
from player.player_reputation import Reputation
from player.player_alignment import Alignment
from combat.combat_stats import CombatStats
from equipment.equipment_manager import EquipmentManager


class Player:

    def __init__(
        self,
        name
    ):

        self.name = name

        self.gold = 100

        self.progression = PlayerProgression()

        self.attributes = Attributes()

        self.resources = PlayerResources()

        self.status = PlayerStatus()

        self.inventory = Inventory()

        self.status_effects = StatusManager()

        self.skills = PlayerSkills()

        self.player_class = (
            DefaultClasses.gunslinger()
        )

        self.background = (
            DefaultBackgrounds.orphan()
        )

        self.reputation = Reputation()

        self.alignment = Alignment.NEUTRAL

        self.traits = []

        self.titles = []

        self.attributes.show()

        self.resources.show()

        self.status.show()

        self.progression.show()

        self.skills.show()

        self.combat = CombatStats(
            self
        )

        self.equipment = EquipmentManager()

    def show_stats(self):

        print(
            f"\n=== {self.name} ==="
        )

        print(
            f"Level: {self.progression.level}"
        )

        print(
            f"XP: {self.progression.experience}"
        )

        print(
            f"Gold: {self.gold}"
        )

        print(
            f"Class: {self.player_class.name}"
        )

        print(
            f"Background: {self.background.name}"
        )

        print(
            f"Alignment: {self.alignment}"
        )

        print("\n=== TRAITS ===")

        for trait in self.traits:

            print(
                f"- {trait}"
            )

        print("\n=== TITLES ===")

        for title in self.titles:

            print(
                f"- {title}"    
            )        

        print("\n=== COMBAT ===")

        print(
            f"Attack: {self.combat.attack_power}"
        )

        print(
            f"Defense: {self.combat.defense}"
        )

        print(
            f"Magic: {self.combat.magic_power}"
        )

        print(
            f"Speed: {self.combat.speed}"
        )

        print(
            f"Crit: {self.combat.crit_chance}%"
        )    

    def gain_experience(
         self,
         amount
):

         self.progression.gain_experience(
         amount
    )
         
    def spend_attribute_point(self):

        if self.attribute_points <= 0:

             return False

        self.attribute_points -= 1

        return True
    
    def spend_skill_point(self):

        if self.skill_points <= 0:

             return False

        self.skill_points -= 1

        return True
    
    def learn_skill(
        self,
        skill_name
):

        self.skills.learn_skill(
            skill_name
    )


    def gain_skill_xp(
        self,
        skill_name,
        amount
):

        self.skills.gain_skill_xp(
            skill_name,
            amount
        )
