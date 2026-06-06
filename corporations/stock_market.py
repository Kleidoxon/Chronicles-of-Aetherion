import random


class StockMarket:
    def update_stock(self, company):
        change = random.randint(-5000, 5000)

        company.value += change

        print(f"{company.name} value changed to {company.value}")