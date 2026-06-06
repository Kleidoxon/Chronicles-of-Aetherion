# player/player_status.py

class PlayerStatus:

    def __init__(self):

        self.is_alive = True

        self.is_in_combat = False

        self.is_wanted = False

        self.is_imprisoned = False

        self.is_corrupted = False

     # Advanced Stats

        self.faith = 0

        self.corruption = 0

        self.sanity = 100

        self.reputation = 0

        self.active_titles = []

    def show(self):

        print("\n=== STATUS ===")

        print(
            f"Alive: {self.is_alive}"
        )

        print(
            f"In Combat: {self.is_in_combat}"
        )

        print(
            f"Wanted: {self.is_wanted}"
        )

        print(
            f"Imprisoned: {self.is_imprisoned}"
        )

        print(
            f"Corrupted: {self.is_corrupted}"
        )