class Business:
    def __init__(self, name, business_type):
        self.name = name
        self.business_type = business_type
        self.level = 1
        self.revenue = 0
        self.staff = []

    def generate_income(self):
        income = self.level * 100
        self.revenue += income

        return income