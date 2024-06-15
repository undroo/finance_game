class World:
    persons = []
    
    def __init__(self, person, region="AUS"):
        self.persons.append(person)
        self.region = region
        self.year = 0

    # We need functions to interact with the person

    def increment_year(self):
        self.year += 1
        self.increment_persons()


    # For each Person, we need to 'grow' their investments and such
    def increment_persons(self):
        # each Person needs to take a 'turn'
        for person in self.persons:
            self.activate_person_turn(person)

    def activate_person_turn(self, person):
        # Automatically update the Persons investment growth and cash before letting them 'act'
        person.start_year_actions(self.year)
        
    