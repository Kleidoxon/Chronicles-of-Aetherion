import random


class ProceduralStory:
    def generate_story(self):
        stories = [
            "A forgotten king rises again",
            "A machine cult controls the parliament",
            "An airship captain discovers ancient ruins",
            "A global trade war begins",
            "A forbidden artifact awakens",
            "A rebellion of machines threatens humanity",
            "A secret society manipulates world events",
            "A plague devastates the population",
            "A powerful AI gains sentience",
            "A holy war erupts between two religions",
            "A charismatic leader unites the world",
            "A hidden city is discovered in the jungle",
            "A mysterious virus spreads across the globe",
        ]

        return random.choice(stories)