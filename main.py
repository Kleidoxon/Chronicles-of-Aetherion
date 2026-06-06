# ==========================================================
# CHRONICLES OF AETHERION
# MAIN ENTRY POINT
# ==========================================================

from engine.bootstrap import Bootstrap


def main():

    game = Bootstrap()

    try:

        game.start()

    except KeyboardInterrupt:

        game.shutdown()


if __name__ == "__main__":

    main()