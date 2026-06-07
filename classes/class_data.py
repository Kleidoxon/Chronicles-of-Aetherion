from dataclasses import dataclass
from classes.class_type import ClassType


@dataclass
class ClassData:

    class_type: ClassType

    hp: int
    mp: int

    attack: int
    defense: int

    crit_rate: float

    description: str