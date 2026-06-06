class Faction:
    # All available factions
    FACTION_NAMES = [
        "Iron Empire",
        "Blackwater Syndicate",
        "Gearwright Consortium",
        "Crimson Brotherhood",
        "Azure Coalition",
        "Shadow Cartel",
        "Golden Dominion",
        "Obsidian Order",
        "Emerald Enclave",
        "Sapphire Alliance",
        "Onyx Legion",
        "Ruby Confederation",
        "Amethyst Guild",
        "Topaz Syndicate",
        "Diamond Consortium",
    ]

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.wealth = 1000
        self.relationships = {}

    def change_relation(self, faction_name, amount):
        if faction_name not in self.relationships:
            self.relationships[faction_name] = 0

        self.relationships[faction_name] += amount