from rich.console import Console


class MenuUI:
    def __init__(self):
        self.console = Console()

    def show_main_menu(self):
        self.console.print("1. Start Game")
        self.console.print("2. Load Game")
        self.console.print("3. Quit")