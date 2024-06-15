from models.investment import Investment

class Cash(Investment):
    growth_rate = [0.05, 0.04, 0.03, 0.04, 0.03, 0.04, 0.03, 0.03, 0.04, 0.03, 0.04, 0.03] # should this be a dictionary based on years? who knows
    asset_status = "Live" # Cash is always 'Live' because there is no capital gains, its fine to have an empty bank account

    # Compared to other investments, we are treating cash differently, mostly because theres no 'dividends' or 'reinvestment'. 
    # By taxing the interest we incur, theres no need to consider capital gains and we can increase the amount freely. Additionally, we may want to add to our pool of cash from selling other investments.

    # No concept of 'selling' cash
    def calculate_tax_on_sell(self):
        return 0 
    
    def add_cash(self, amount):
        self.amount += amount

    def spend_cash(self, amount):
        self.amount -= amount
    
