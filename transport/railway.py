class Railway:
    def __init__(self):
        self.routes = []

    def add_route(self, city_a, city_b):
        self.routes.append((city_a, city_b))

        print(f"Route added: {city_a} -> {city_b}")