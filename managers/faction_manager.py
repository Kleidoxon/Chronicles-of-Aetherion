# managers/faction_manager.py

from factions.faction import Faction
from factions.diplomacy import Diplomacy
from factions.war_system import WarSystem


class FactionManager:

    def __init__(self):

        self.factions = {}

        self.diplomacy = Diplomacy()

        self.war_system = WarSystem()

    def create_faction(
        self,
        faction_name
    ):

        faction = Faction(
            faction_name
        )

        self.factions[faction_name] = faction

        return faction

    def get_faction(
        self,
        faction_name
    ):

        return self.factions.get(
            faction_name
        )

    def declare_war(
        self,
        attacker,
        defender
    ):

        self.war_system.declare_war(
            attacker,
            defender
        )

    def create_alliance(
        self,
        faction_a,
        faction_b
    ):

        self.diplomacy.create_alliance(
            faction_a,
            faction_b
        )

    def process_turn(self):

        self.diplomacy.update()

        self.war_system.update()

    def update(self):

        print(
            "Faction Updated"
        )