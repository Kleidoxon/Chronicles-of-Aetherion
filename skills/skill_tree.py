class Skill:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def upgrade(self):
        self.level += 1