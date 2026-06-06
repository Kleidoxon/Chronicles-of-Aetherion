class Treaty:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show_treaty(self):
        print(f"Treaty: {self.name}")
        print(f"Duration: {self.duration}")