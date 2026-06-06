# managers/economy_manager.py

from economy.simple_market import SimpleMarket
from economy.advanced_market import AdvancedMarket

from ownership.business import Business

from governance.city_taxation import CityTaxation


class EconomyManager:
   
    def __init__(self):

        self.market = SimpleMarket()

        self.advanced_market = AdvancedMarket()

        self.taxation = CityTaxation()

        self.businesses = []

    def update_market(self):

        self.market.update()

    def register_business(
        self,
        business_name
    ):

        business = Business(
            business_name
        )

        self.businesses.append(
            business
        )

        return business

    def collect_tax(self, amount):

        return self.taxation.collect_tax(
            amount
        )
    
    def on_business_created(
        self,
        context 
    ):
        business_name = context.get(
            "business_name"
        )

        print(
            f"Economy reacting to new business: {business_name}"
        )
    def update(self):

        print(
            "Economy Updated"
        )