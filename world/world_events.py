import random


class WorldEvents:
    def random_event(self):
        events = [
            "Market Crash",
            "Steam Riot",
            "Railway Expansion",
            "Political Assassination",
            "Mine Collapse",
            "Factory Fire",
            "Technological Breakthrough",
            "Labor Strike",
            "Currency Devaluation",
            "Epidemic Outbreak",
            "Natural Disaster",
            "Cultural Festival",
            "Scientific Discovery",
            "Military Conflict",
            "Diplomatic Summit",
            "Infrastructure Boom",
            "Social Unrest",
            "Technological Malfunction",
            "Economic Boom",
            "Resource Shortage",
            "Environmental Crisis",
            "Public Health Crisis",
            "Technological Innovation",
            "Cultural Renaissance",
            "Political Scandal",
            "Labor Strike",
            "Civil Unrest",
        
        ]

        return random.choice(events)