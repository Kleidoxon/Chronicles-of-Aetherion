# simulation/tick_processor.py


class TickProcessor:

    def __init__(self):

        self.tick = 0

    def advance_tick(self):

        self.tick += 1

    def get_tick(self):

        return self.tick