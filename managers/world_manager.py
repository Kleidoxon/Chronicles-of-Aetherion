# managers/world_manager.py

from world.city_system import City
from world.world_events import WorldEvents

from map.procedural_map import ProceduralMap

from environment.restoration_system import RestorationSystem
from environment.permanent_damage import PermanentDamage
from environment.climate_balance import ClimateBalance


class WorldManager:

    def __init__(self):

        self.world_events = WorldEvents()

        self.map_generator = ProceduralMap()

        self.restoration = RestorationSystem()

        self.damage = PermanentDamage()

        self.climate = ClimateBalance()

        self.cities = []

    def generate_world(self):

        self.map_generator.generate()

    def create_city(self, city_name):

        city = City(city_name)

        self.cities.append(city)

        return city

    def trigger_world_event(self):

        return self.world_events.random_event()

    def restore_environment(self):

        self.restoration.restore_forest()

    def apply_mining_damage(self):

        self.damage.apply_mining_damage()