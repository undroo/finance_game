from interfaces.taxation import *

class IndividualTaxReport():
    capital_gains = 0
    deductions = 0

    def __init__(self, year, income, previous_year_cgt_losses=0) -> None:
        self.year = year
        self.income = income
        self.total_income = income
        self.capital_gains = previous_year_cgt_losses
        self.tax_due = self.calculate_tax_due()

    # Should this be a line-by-line breakdown? its not in the real tax report though.
    def add_cgt_event(self, amount):
        self.capital_gains += amount
        self.total_income += amount

    def add_deductions(self,amount):
        self.deductions += amount

    def calculate_tax_due(self):
        return calculate_individual_tax(self.total_income)
    
