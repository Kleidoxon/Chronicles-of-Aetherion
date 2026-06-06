class Parliament:
    def __init__(self):
        self.laws = []

    def pass_law(self, law):
        self.laws.append(law)

        print(f"Law Passed: {law}")