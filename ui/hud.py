class HUD:
    def display_hud(self, player):
        print(f"HP: {player.health}")
        print(f"Mana: {player.mana}")
        print(f"Gold: {player.gold}")