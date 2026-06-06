# combat/status_manager.py



class StatusManager:

    def __init__(self):

        self.active_effects = {}

    # =====================================
    # APPLY
    # =====================================

    def apply_effect(
        self,
        target,
        effect
    ):

        if target not in self.active_effects:

            self.active_effects[target.name] = []

        self.active_effects[target.name].append(
            effect
        )

        print(
            f"{target.name} gains "
            f"{effect.name}"
        )

    # =====================================
    # PROCESS TURN
    # =====================================

    def process_turn(self):

        for target in list(
            self.active_effects.keys()
        ):

            remaining = []

            for effect in self.active_effects[target.name]:

                if effect.damage_per_turn:

                 if hasattr(target, "resources"):

                    target.resources.health -= (
                        effect.damage_per_turn
                    )
                    print(
                        f"{target.name} suffers "
                        f"{effect.damage_per_turn}"
                        f" damage from "
                        f"{effect.name}"
                    )

                if effect.healing_per_turn:

                    target.resources.health += (
                        effect.healing_per_turn
                    )
                    print(
                        f"{target.name} heals "
                        f"{effect.healing_per_turn}"
                        f" health from "
                        f"{effect.name}"
                    )

                effect.tick()

                if not effect.expired():

                    remaining.append(
                        effect
                    )

                else:

                    print(
                        f"{effect.name}"
                        f" expired on "
                        f"{target}"
                    )
        if remaining:

            self.active_effects[target] = remaining

        else:

            del self.active_effects[target.name]

    # =====================================
    # DEBUG
    # =====================================

    def show_effects(self):

        for target, effects in (
            self.active_effects.items()
        ):

            print(f"\n{target}")

            for effect in effects:

                print(
                    f" - {effect}"
                )

    def show(self):

        print("\n=== STATUS ===")

        print(
            f"Stunned: {self.is_stunned}"
        )

        print(
            f"Silenced: {self.is_silenced}"
        )

        print(
            f"Feared: {self.is_Feared}"
        )

        print(
            f"Frozen: {self.is_frozen}"
        )

        print(
            f"Burning: {self.is_burning}"
        )