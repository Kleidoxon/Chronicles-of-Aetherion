# engine/bootstrap.py

from engine.world_runtime import WorldRuntime
from engine.service_container import ServiceContainer
from engine.game_state import GameState
from engine.event_bus import EventBus
from engine.scheduler import Scheduler

from simulation.tick_processor import TickProcessor

from managers.ai_manager import AIManager
from managers.economy_manager import EconomyManager
from managers.ownership_manager import OwnershipManager
from managers.governance_manager import GovernanceManager
from managers.faction_manager import FactionManager
from managers.world_manager import WorldManager
from managers.dimension_manager import DimensionManager
from managers.universe_manager import UniverseManager
from managers.codex_manager import CodexManager

from managers.player_manager import PlayerManager
from managers.combat_manager import CombatManager
from managers.quest_manager import QuestManager
from managers.simulation_manager import SimulationManager

class Bootstrap:

    def __init__(self):

        self.services = ServiceContainer()

        self.game_state = GameState()

        self.event_bus = EventBus()

        self.scheduler = Scheduler()

        self.tick_processor = TickProcessor()

        self.runtime = None

    # =====================================
    # REGISTER SERVICES
    # =====================================

    def register_services(self):

        self.services.register(
            "ai_manager",
            AIManager()
        )

        self.services.register(
            "economy_manager",
            EconomyManager()
        )

        self.services.register(
            "ownership_manager",
            OwnershipManager()
        )

        self.services.register(
            "governance_manager",
            GovernanceManager()
        )

        self.services.register(
            "faction_manager",
            FactionManager()
        )

        self.services.register(
            "world_manager",
            WorldManager()
        )

        self.services.register(
            "dimension_manager",
            DimensionManager()
        )

        self.services.register(
            "universe_manager",
            UniverseManager()
        )

        self.services.register(
            "codex_manager",
            CodexManager()
        )

        self.services.register(
            "player_manager",
            PlayerManager()
)

        self.services.register(
            "combat_manager",
            CombatManager()
)

        self.services.register(
            "quest_manager",
            QuestManager()
)

        self.services.register(
            "simulation_manager",
            SimulationManager()
)

        print("\nManagers Registered:")

        print(
            self.services.list_services()
        )

    # =====================================
    # CREATE RUNTIME
    # =====================================

    def create_runtime(self):

        self.runtime = WorldRuntime(
            self.services,
            self.event_bus,
            self.tick_processor
        )

    # =====================================
    # START
    # =====================================

    def start(self):

        self.register_services()

        print("\n=== REGISTERED SERVICES ===")

        for service in self.services.list_services():
            print(service)

        print("===========================\n")

        self.create_runtime()

        print(
            "\nChronicles of Aetherion Started\n"
        )

        while True:

            self.runtime.update()

            command = input(
                "\nPress ENTER for next tick or type EXIT: "
            )

            if command.lower() == "exit":

                self.shutdown()

                break

    # =====================================
    # SHUTDOWN
    # =====================================

    def shutdown(self):

        print(
            "\nSaving World..."
        )

        print(
            "Shutdown Complete."
        )