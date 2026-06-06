import json


class SaveManager:
    def save_game(self, player, city, filename="savegame.json"):
        data = {
            "player": {
                "name": player.name,
                "level": player.level,
                "gold": player.gold,
                "health": player.health
            },
            "city": {
                "name": city.name,
                "wealth": city.wealth,
                "population": city.population
            }
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Game Saved")

    def load_game(self, filename="savegame.json"):
        with open(filename, "r") as file:
            data = json.load(file)

        print("Game Loaded")

        return data