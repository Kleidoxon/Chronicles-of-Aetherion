import random


class CrimeSystem:
    def commit_crime(self):
        crimes = [
            "Robbery",
            "Smuggling",
            "Illegal Mining",
            "Bribery",
            "Assassination",
            "Forgery",
            "Extortion",
            "Kidnapping",
            "Piracy",
            "Blackmail",
            "Counterfeiting",
            "Vandalism",
            "Cybercrime",
            "Drug Trafficking",
            "Human Trafficking",
            "Arson",
            "Gambling",
            "Prostitution",
            "Money Laundering",
            "Terror Attack"
        ]

        return random.choice(crimes)