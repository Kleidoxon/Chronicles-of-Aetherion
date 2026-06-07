from classes.class_type import ClassType
from classes.class_data import ClassData


CLASS_REGISTRY = {

    ClassType.WARRIOR: ClassData(
        class_type=ClassType.WARRIOR,
        hp=150,
        mp=40,
        attack=20,
        defense=15,
        crit_rate=0.05,
        description="Frontline fighter."
    ),

    ClassType.MAGE: ClassData(
        class_type=ClassType.MAGE,
        hp=80,
        mp=200,
        attack=30,
        defense=5,
        crit_rate=0.05,
        description="Master of elemental magic."
    ),

    ClassType.NECROMANCER: ClassData(
        class_type=ClassType.NECROMANCER,
        hp=90,
        mp=220,
        attack=35,
        defense=5,
        crit_rate=0.10,
        description="Commands the dead."
    ),
}

def get_class_data(class_type):
    return CLASS_REGISTRY[class_type]