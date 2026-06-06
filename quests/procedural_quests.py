import random


class QuestGenerator:
    def generate_quest(self):
        objectives = [
            "Eliminate Smugglers",
            "Protect Airship",
            "Deliver Secret Cargo",
            "Hunt Steam Beast",
            "Escort Merchant"
        ]

        rewards = [100, 200, 500, 1000]

        return {
            "objective": random.choice(objectives),
            "reward": random.choice(rewards)
        }