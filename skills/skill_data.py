from classes.class_type import ClassType


CLASS_SKILLS = {

    ClassType.WARRIOR: [
        "Slash",
        "Shield Bash",
    ],

    ClassType.MAGE: [
        "Fireball",
        "Ice Lance",
    ],

    ClassType.NECROMANCER: [
        "Raise Skeleton",
        "Death Bolt",
    ]
}


def get_skills(class_type):
    return CLASS_SKILLS.get(class_type, [])