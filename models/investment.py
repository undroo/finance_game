from interfaces.taxation import *

class Investment:
    growth_rate = [0.08, 0.06, 0.07, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05] # should this be a dictionary based on years? or needs to be generated from another function
    asset_status = "Live" # Convert to "Sold" when the asset is sold

    def __init__(self, amount, year):
        self.amount = amount
        self.year = year
        self.buy_price = amount
        self.year_bought = year

    def sell_asset(self):
        # calculate tax owing
        # convert asset status to sold? 
        pass

    def calculate_tax_on_sell(self):
        tax_discount = 1
        if self.year - self.year_bought >= 1: 
            # tax is halved
            tax_discount = 0.5
        tax_due = calculate_individual_tax(self.amount - self.buy_price) * tax_discount
        return tax_due

    def grow_asset(self, year):
        self.amount = self.amount * (1+self.growth_rate[year-1])
        self.year = year
 
    def sell_asset(self):
        tax_due = self.calculate_tax_on_sell()
        result = {
            "cash": self.amount,
            "tax due": tax_due,
        }
        self.amount = 0
        self.asset_status = "Sold"
        return result