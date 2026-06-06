class Panel:
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering panel: {self.name}")