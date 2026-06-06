import random


class AmbitionSystem:
    def choose_goal(self):
        goals = [
            "Become Rich",
            "Conquer Cities",
            "Start Religion",
            "Control Trade",
            "Destroy Rivals",
            "Seek Knowledge",
            "Expand Territory",
            "Form Alliances",
            "Dominate the World",
            "Achieve Immortality",
            "Create a Dynasty",
            "Amass Power",
            "Spread Influence",
            "Build Wonders",
            "Uncover Secrets",
            "Revolutionize Society",
            "Master Magic",
            "Lead a Rebellion",
            "Discover New Lands",
            "Invent New Technology",
            "Become a Legend",
            "Unite Factions",
            "Defend the Realm",
            "Overthrow the Government",
            "Establish a Legacy",
            "Control the Seas",
            "Harness Natural Resources",
            "Become a Patron of the Arts",
            "Create a Cult",
            "Achieve Enlightenment",
            "Dominate the Skies",
            "Conquer the Underworld",
            "Master the Elements",
            "Unleash Chaos",
            "Forge a New World",
            "Become a Hero",
            "Seek Revenge",
            "Build a Great Army",
            "Control the Economy",
        ]

        return random.choice(goals)