# managers/simulation_manager.py

from simulation.world_tick import WorldTick


class SimulationManager:

    def __init__(self):

        self.world_tick = WorldTick()

        self.tick_count = 0

    def advance_tick(self):

        self.tick_count += 1

        self.world_tick.update()

    def get_tick(self):

        return self.tick_count

    def update(self):

        self.advance_tick()

        print(
            f"Simulation Tick {self.tick_count}"
        )