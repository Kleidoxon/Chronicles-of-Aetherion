# ==========================================================
# CHRONICLES OF AETHERION
# MAIN ENTRY POINT
# ==========================================================

from engine.bootstrap import Bootstrap
from characters.player import Player
from classes.class_type import ClassType



def main():

    game = Bootstrap()

    try:

        game.start()

    except KeyboardInterrupt:

        game.shutdown()


if __name__ == "__main__":

    main()

player = Player("Arthur")

player.display()

player.evolve(
    ClassType.NECROMANCER
)

print()

player.display()    
