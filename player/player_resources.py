# player/player_resources.py

class PlayerResources:

    def __init__(self):

        self.max_health = 100
        self.health = 100

        self.max_mana = 50
        self.mana = 50

        self.max_stamina = 100
        self.stamina = 100

    def take_damage(
        self,
        amount
    ):

        self.health -= amount

        if self.health < 0:

            self.health = 0

    def heal(
        self,
        amount
    ):

        self.health += amount

        if self.health > self.max_health:

            self.health = self.max_health

    def restore_mana(
        self,
        amount
    ):

        self.mana += amount

        if self.mana > self.max_mana:

            self.mana = self.max_mana

    def restore_stamina(
        self,
        amount
    ):

        self.stamina += amount

        if self.stamina > self.max_stamina:

            self.stamina = self.max_stamina

    def show(self):

        print("\n=== RESOURCES ===")

        print(
            f"HP: {self.health}/{self.max_health}"
        )

        print(
            f"MP: {self.mana}/{self.max_mana}"
        )

        print(
            f"STA: {self.stamina}/{self.max_stamina}"
        )

    def recalculate(
        self,
        attributes
):
        
        self.max_health = (
            100 +
            attributes.vitality * 10
        )

        self.max_mana = (
            50 +
            attributes.intelligence * 5
        )

        self.max_stamina = (
            100 +
            attributes.dexterity * 5
        )