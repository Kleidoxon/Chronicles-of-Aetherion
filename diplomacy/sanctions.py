class Sanction:
    def apply_sanction(self, faction):
        faction.wealth -= 500

        print(f"Sanctions applied to {faction.name}")