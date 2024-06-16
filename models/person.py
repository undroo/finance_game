from models.job import Job
from models.investment import Investment
from models.cash import Cash
from models.individual_tax_report import IndividualTaxReport


class Person:
    # to keep it simple lets use a savings rate of 30%
    savings_rate = 0.3
    
    tax_reports = {}
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
        # Need to build an 'expenses'

    # Each year, a person will have the opportunity to make decisions with their money. Their money comes from their existing investments and its growth as well as any savings incurred during the year.
    def start_year_actions(self,year):
        self.tax_set_aside = 0
        self.grow_assets(year)
        # function to change income?
        self.year+=1
        self.tax_reports[year] = IndividualTaxReport(self.year, self.job.total_income)
        self.current_tax_report = self.tax_reports[year]
        # Income earning
        self.earn_salary()
        # receive dividends somehow


        # ----- Random stuff ----------- # 
        print(year, "cash at start", self.cash.amount)
        self.actions_for_year()
        # delete later
        self.print_investments()
        print(year, "total income: ", self.current_tax_report.total_income)
        print(year, "cash at turn end:", self.cash.amount)
        print(year, "tax paid: ", self.tax_set_aside)
        print(year, "net value at turn end: ", self.get_total_asset_value())

        # -------- End of year ---------- # 
        # pay tax
        

    
    def earn_salary(self):
        # tax_from_job = self.job.get_after_tax_income()
        # savings = self.savings_rate * tax_from_job # maybe this be separated so we can create a 'tax report'
        # self.cash.add_cash(savings)
        
        gross_income = self.job.get_gross_income()
        self.cash.add_cash(gross_income)
        tax_due = self.current_tax_report.calculate_tax_due()
        self.tax_set_aside = tax_due
        self.cash.spend_cash(tax_due)
    
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
            capital_gains = result['capital_gains']

            # Add capital gains to tax report and set aside cash
            self.current_tax_report.add_cgt_event(capital_gains)
            additional_tax_due = self.current_tax_report.calculate_tax_due() - self.tax_set_aside
            self.tax_set_aside = self.current_tax_report.calculate_tax_due()
            self.cash.spend_cash(additional_tax_due)

            # self.cash.spend_cash(tax_due) # eventually need to add a taxation report

    def get_total_asset_value(self):
        total = 0
        total += self.cash.amount
        for i in self.investments:
            total += i.amount
        return total
    
    def calculate_tax_due(self):
        pass
    # --------------------------------------------------------------------------------------- # 
    
    # Helper functions, probably delete later. 
    

    # These act as manual tests of the functions by using pre-determined behaviour
    def actions_for_year(self):
        # who knows how this works, for now lets make some stuff up

        # every year, you use 50% of your cash to buy stocks
        amount_to_invest = 0.2 * self.cash.amount
        amount_to_spend = 0.5 * self.cash.amount
        self.cash.spend_cash(amount_to_spend)
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