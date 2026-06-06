class Taxation:
    TAX_RATE = 0.15

    def calculate_tax(self, revenue):
        return revenue * self.TAX_RATE

    def collect_business_tax(self, business):
        tax = self.calculate_tax(business.revenue)
        print(f"Collected {tax} gold taxes from {business.name}")
        return tax