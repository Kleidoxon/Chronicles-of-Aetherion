class Religion:
    def __init__(self, name, doctrine):
        self.name = name
        self.doctrine = doctrine
        self.followers = 0

    def gain_followers(self, amount):
        self.followers += amount