# player/player_progression.py


class PlayerProgression:

    def __init__(self):

        self.level = 1

        self.experience = 0

        self.experience_to_next = 100

        self.skill_points = 0

        self.attribute_points = 0

    # =====================================
    # EXPERIENCE
    # =====================================

    def gain_experience(
        self,
        amount
    ):

        self.experience += amount

        print(
            f"Gained {amount} XP"
        )

        while (
            self.experience
            >= self.experience_to_next
        ):

            self.level_up()

    # =====================================
    # LEVEL UP
    # =====================================

    def level_up(self):

        self.experience -= (
            self.experience_to_next
        )

        self.level += 1

        self.skill_points += 2

        self.attribute_points += 5

        self.experience_to_next = int(
            self.experience_to_next * 1.25
        )

        print(
            f"\nLEVEL UP!"
        )

        print(
            f"Reached Level {self.level}"
        )

    # =====================================
    # INFO
    # =====================================

    def show(self):

        print(
            "\n=== PROGRESSION ==="
        )

        print(
            f"Level: {self.level}"
        )

        print(
            f"XP: "
            f"{self.experience}/"
            f"{self.experience_to_next}"
        )

        print(
            f"Skill Points: "
            f"{self.skill_points}"
        )

        print(
            f"Attribute Points: "
            f"{self.attribute_points}"
        )