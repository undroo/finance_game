from models.job import Job
from models.investment import Investment
from models.cash import Cash


class Person:
    # to keep it simple lets use a savings rate of 30%
    savings_rate = 0.3
    
    # assumptions
    year = 0 # do Person need to know this?
    # do we need to create some sort of history?

    def __init__(self, job, investments=[], region="AUS"):
        self.job = job
        self.investments = investments
        self.region = region
        
        # Let's assume everyone has a bank account for cash
        # Also assume Person is only created in year 0.
        # Let's keep cash separate for ease of access over time
        self.cash = Cash(amount=0, year=0)


    # Each year, a person will have the opportunity to make decisions with their money. Their money comes from their existing investments and its growth as well as any savings incurred during the year.
    def start_year_actions(self,year):
        self.grow_assets(year)
        self.add_savings()
        print(year, "cash at start", self.cash.amount)
        # Increment year before allowing them to 
        self.year+=1
        self.actions_for_year()
        

        # delete later
        self.print_investments()
        print(year, "cash at turn end:", self.cash.amount)
        print(year, "net value at turn end: ", self.get_total_asset_value())
        

    
    def add_savings(self):
        tax_from_job = self.job.get_after_tax_income()
        savings = self.savings_rate * tax_from_job # maybe this be separated so we can create a 'tax report'
        self.cash.add_cash(savings)
    
    # grow investments after you 'decide' what to do with your money for the year but doesn't apply for the year you buy it in.
    def grow_assets(self, year):
        for investment in self.investments:
            investment.grow_asset(year)
        self.cash.grow_asset(year)

    # eventually we make one of these for each 'type' of investment
    def add_investment(self, amount):
        investment = Investment(amount=amount, year=self.year)
        self.investments.append(investment)
        
    def buy_investment(self, amount):
        self.cash.spend_cash(amount)
        self.add_investment(amount)

    def sell_investment(self, investment):
        if investment in self.investments:
            result = investment.sell_asset()
            self.cash.add_cash(result['cash'])
            tax_due = result['tax due']
            self.cash.spend_cash(tax_due) # eventually need to add a taxation report

    def get_total_asset_value(self):
        total = 0
        total += self.cash.amount
        for i in self.investments:
            total += i.amount
        return total

    # --------------------------------------------------------------------------------------- # 
    
    # Helper functions, probably delete later. 
    

    # These act as manual tests of the functions by using pre-determined behaviour
    def actions_for_year(self):
        # who knows how this works, for now lets make some stuff up

        # every year, you use 50% of your cash to buy stocks
        amount_to_invest = 0.5 * self.cash.amount
        self.buy_investment(amount_to_invest)

        if self.year == 5:
            # lets test selling everything
            for i in self.investments:
                # print("selling investment", self.year, i.amount)
                self.sell_investment(i)


    def print_investments(self):
        for investment in self.investments:
            print(self.year, "investment", investment.amount)

    # --------------------------------------------------------------------------------------- # 