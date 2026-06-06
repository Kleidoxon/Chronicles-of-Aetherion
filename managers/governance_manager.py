# managers/governance_manager.py

from governance.governance_simulation import GovernanceSimulation
from governance.city_taxation import CityTaxation
from governance.corruption_system import CorruptionSystem


class GovernanceManager:

    def __init__(self):

        self.governance = GovernanceSimulation()

        self.taxation = CityTaxation()

        self.corruption = CorruptionSystem()

    # =====================================
    # GOVERN CITY
    # =====================================

    def govern_city(
        self,
        city
    ):

        self.governance.govern_city(
            city
        )

    # =====================================
    # TAX COLLECTION
    # =====================================

    def collect_tax(
        self,
        amount
    ):

        return self.taxation.collect_tax(
            amount
        )

    # =====================================
    # CORRUPTION
    # =====================================

    def update_corruption(self):

        self.corruption.spread_corruption()

    # =====================================
    # TURN PROCESSING
    # =====================================

    def process_turn(self):

        self.update_corruption()

    # =====================================
    # EVENT HANDLER
    # =====================================

    def on_tax_collected(
        self,
        context
    ):

        print(
            "Government revenue increased."
        )

    # =====================================
    # PHASE 9 STANDARD UPDATE
    # =====================================

    def update(self):

        self.process_turn()

        print(
            "Governance Updated"
        )