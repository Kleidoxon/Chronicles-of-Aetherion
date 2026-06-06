# managers/dimension_manager.py

from dimensions.dimensional_generator import DimensionalGenerator
from dimensions.dimensional_travel import DimensionalTravel

from reality.reality_manipulation import RealityManipulation

from game_time.time_travel import TimeTravel


class DimensionManager:

    def __init__(self):

        self.generator = DimensionalGenerator()

        self.travel = DimensionalTravel()

        self.reality = RealityManipulation()

        self.time_travel = TimeTravel()

        self.active_dimensions = []

    def generate_dimension(self):

        dimension = self.generator.generate()

        self.active_dimensions.append(
            dimension
        )

        return dimension

    def travel_dimension(
        self,
        traveler,
        destination
    ):

        self.travel.travel(
            traveler,
            destination
        )

    def update(self):
        print(
            "Dimensions Updated"
        )
        pass