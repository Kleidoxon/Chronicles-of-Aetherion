# player/player_skills.py

from skills.magic_mastery import MagicMastery
from skills.massive_skill_tree import MassiveSkillTree


class PlayerSkills:

    def __init__(self):

        self.magic_mastery = MagicMastery()

        self.skill_tree = MassiveSkillTree()

        self.learned_skills = {}

    # =====================================
    # LEARN SKILL
    # =====================================

    def learn_skill(
        self,
        skill_name
    ):

        if skill_name in self.learned_skills:

            return

        self.learned_skills[
            skill_name
        ] = {
            "level": 1,
            "xp": 0
        }

        print(
            f"Learned Skill: {skill_name}"
        )

    # =====================================
    # GAIN XP
    # =====================================

    def gain_skill_xp(
        self,
        skill_name,
        amount
    ):

        if (
            skill_name
            not in self.learned_skills
        ):
            return

        self.learned_skills[
            skill_name
        ]["xp"] += amount

        self.check_level_up(
            skill_name
        )

    # =====================================
    # LEVEL UP
    # =====================================

    def check_level_up(
        self,
        skill_name
    ):

        skill = self.learned_skills[
            skill_name
        ]

        needed = (
            skill["level"] * 100
        )

        while skill["xp"] >= needed:

            skill["xp"] -= needed

            skill["level"] += 1

            needed = (
                skill["level"] * 100
            )

            print(
                f"{skill_name} "
                f"reached level "
                f"{skill['level']}"
            )

    # =====================================
    # SHOW
    # =====================================

    def show(self):

        print(
            "\n=== SKILLS ==="
        )

        if not self.learned_skills:

            print("No skills learned.")

            return

        for (
            name,
            data
        ) in self.learned_skills.items():

            print(
                f"{name} "
                f"(Lv {data['level']})"
            )