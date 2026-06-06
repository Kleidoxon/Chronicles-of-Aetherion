import random


class WarSystem:
    def simulate_war(self, faction_a, faction_b):
        power_a = faction_a.power + random.randint(1, 100)
        power_b = faction_b.power + random.randint(1, 100)

        if power_a > power_b:
            spoils = power_b * 10
            faction_a.wealth += spoils

            print(f"{faction_a.name} wins the war")
            print(f"Spoils gained: {spoils}")

        else:
            spoils = power_a * 10
            faction_b.wealth += spoils

            print(f"{faction_b.name} wins the war")
            print(f"Spoils gained: {spoils}")