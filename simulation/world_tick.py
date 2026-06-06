import time


class WorldTick:
    def __init__(self):
        self.day = 1
        self.hour = 0

    def tick(self):
        self.hour += 1

        if self.hour >= 24:
            self.hour = 0
            self.day += 1

        print(f"Day {self.day} | Hour {self.hour}")

        time.sleep(1)   