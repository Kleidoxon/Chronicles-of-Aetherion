import random


class PersonalityEngine:
    def generate_personality(self):
        personalities = [
            "Aggressive",
            "Greedy",
            "Merciful",
            "Manipulative",
            "Paranoid",
            "Honorable",
            "Cunning",
            "Loyal",
            "Deceptive",
            "Charismatic",
            "Cowardly",
            "Brave",
            "Compassionate",
            "Ruthless",
            "Optimistic",
            "Pessimistic",
            "Adventurous",
            "Cautious",
            "Reckless",
            "Calculating",
            "Impulsive",
            "Diplomatic",
            "Hostile",
            "Trusting",
            "Suspicious",
            "Generous",
            "Selfish",
            "Patient",
            "Impatient",
            "Creative",
            "Conservative",
            "Innovative",
            "Traditional",
            "Pragmatic",
            "Idealistic",
            "Skeptical",
            "Naive",
        ]

        return random.choice(personalities)