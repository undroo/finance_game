from interfaces.taxation import *

class Job:

    def __init__(self, base, bonus, super_rate=0.11):
        self.base = base
        self.bonus = bonus
        self.total_income = base + bonus
        self.super_dollars = (base+bonus)*super_rate
        # need to call the tax rate calculator interface here

    def get_gross_income(self):
        return self.total_income

    def get_after_tax_income(self):
        tax_due = calculate_individual_tax(self.total_income)
        after_tax_income = self.total_income - tax_due
        return after_tax_income

    def get_after_tax_super(self):
        tax_due = calculate_super_tax(self.super_dollars)
        return self.super_dollars - tax_due