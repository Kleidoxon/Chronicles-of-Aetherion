# simulation/simulation_loop.py

import time


class SimulationLoop:

    def __init__(self):

        self.running = False

        self.systems = []

    # =====================================
    # REGISTER SYSTEM
    # =====================================

    def register_system(
        self,
        system
    ):

        self.systems.append(
            system
        )

    # =====================================
    # START LOOP
    # =====================================

    def start(self):

        self.running = True

        while self.running:

            for system in self.systems:

                if hasattr(
                    system,
                    "update"
                ):

                    system.update()

            time.sleep(1)

    # =====================================
    # STOP LOOP
    # =====================================

    def stop(self):

        self.running = False