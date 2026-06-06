class Staff:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.happiness = 50

    def pay_salary(self):
        print(f"Paid {self.salary} gold to {self.name}")