import random
from factions.faction import Faction
from factions.diplomacy import Diplomacy


class FactionAI:
    def __init__(self):
        # Get faction names from Faction class
        faction_names = Faction.FACTION_NAMES
        # Create Faction objects and store them by name
        self.factions = {name: Faction(name, power=random.randint(50, 100)) for name in faction_names}
        self.diplomacy = Diplomacy()

    def update_factions(self):
        # Get a random faction object by name
        faction_name = random.choice(list(self.factions.keys()))
        faction = self.factions[faction_name]

        actions = [
            ("Started a war", 5, -15, "war"),
            ("Expanded territory", 10, 20, "neutral"),
            ("Manipulated the market", 7, 10, "neutral"),
            ("Built a factory", 7, 15, "neutral"),
            ("Launched a propaganda campaign", 6, 5, "neutral"),
            ("Assassinated a rival leader", 3, 10, "war"),
            ("Initiated a trade embargo", 4, -10, "war"),
            ("Formed an alliance", 8, 8, "alliance"),
            ("Sabotaged a rival's infrastructure", 4, -20, "war"),
            ("Stole technology", 6, 12, "war"),
            ("Developed a new weapon", 5, 18, "neutral"),
            ("Recruited mercenaries", 5, -50, "neutral"),
            ("Launched a cyber attack", 4, 8, "war"),
            ("Corrupted a city official", 3, 5, "neutral"),
            ("Formed a Trade Agreement", 8, 30, "alliance"),
            ("Formed a Military Alliance", 7, 15, "alliance"),
            ("Declared War on a Rival Faction", 3, -25, "war"),
            ("Sabotaged a Rival Faction's Factory", 4, -15, "war"),
            ("Bribed a City Official", 5, -20, "neutral"),
            ("Spread Propaganda", 6, 8, "war"),
            ("Assassinated a Rival Faction Leader", 1, -10, "war"),
            ("Stole Technology from a Rival Faction", 4, 15, "war"),
            ("Expanded Territory into a Rival Faction's Region", 5, 25, "war"),
            ("Formed a Secret Alliance with a Rival Faction", 2, 10, "alliance"),
            ("Initiated a Trade Embargo against a Rival Faction", 3, -12, "war"),
            ("Recruited Mercenaries to Attack a Rival Faction", 4, -40, "war"),
        ]

        action_texts = [text for text, percent, power_change, diplo_type in actions]
        action_weights = [percent for text, percent, power_change, diplo_type in actions]
        power_changes = [power_change for text, percent, power_change, diplo_type in actions]
        diplo_types = [diplo_type for text, percent, power_change, diplo_type in actions]
        
        action_index = random.choices(range(len(actions)), weights=action_weights, k=1)[0]
        action = action_texts[action_index]
        power_change = power_changes[action_index]
        diplo_type = diplo_types[action_index]
        
        # Apply power change to faction
        faction.power += power_change
        faction.power = max(0, faction.power)  # Prevent negative power
        
        print(f"{faction.name} {action} (Power: {faction.power})")
        
        # Generate diplomatic interactions for actions that involve other factions
        self.generate_diplomatic_events(faction, action, diplo_type)
    
    def generate_diplomatic_events(self, faction, action, diplo_type):
        """Generate diplomatic interactions based on faction actions"""
        # Get all other factions
        other_factions = [f for fname, f in self.factions.items() if fname != faction.name]
        
        if not other_factions:
            return
        
        # Select target faction(s) based on action type
        if diplo_type == "alliance":
            target = random.choice(other_factions)
            self.diplomacy.alliance(faction, target)
            
        elif diplo_type == "war":
            target = random.choice(other_factions)
            self.diplomacy.declare_war(faction, target)
        
        elif diplo_type == "neutral":
            # Random minor relationship changes
            target = random.choice(other_factions)
            change = random.randint(-5, 5)
            faction.change_relation(target.name, change)
    
    def trigger_diplomatic_event(self, faction_a_name, faction_b_name, event_type):
        """Manually trigger a diplomatic event between two factions"""
        faction_a = self.get_faction_by_name(faction_a_name)
        faction_b = self.get_faction_by_name(faction_b_name)
        
        if not faction_a or not faction_b:
            print(f"Error: One or both factions not found")
            return
        
        if event_type == "alliance":
            self.diplomacy.alliance(faction_a, faction_b)
        elif event_type == "war":
            self.diplomacy.declare_war(faction_a, faction_b)
        else:
            print(f"Unknown event type: {event_type}")
    
    def get_faction_by_name(self, name):
        """Get a faction object by its name"""
        return self.factions.get(name)
    
    def get_all_factions(self):
        """Get all faction objects"""
        return self.factions
    
    def get_faction_relationships(self, faction_name):
        """Get all relationships for a specific faction"""
        faction = self.get_faction_by_name(faction_name)
        if faction:
            return faction.relationships
        return None