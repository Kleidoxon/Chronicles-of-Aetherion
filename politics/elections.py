import random


class Election:
    def hold_election(self, candidates):
        winner = random.choice(candidates)

        print(f"Election Winner: {winner}")

        return winner