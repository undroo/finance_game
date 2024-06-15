from models.job import Job
from models.person import Person
from models.world import World


job = Job(
    base=100000,
    bonus=10000,
)
person = Person(job=job)

world = World(person=person)
world.increment_year()
world.increment_year()
world.increment_year()
world.increment_year()
world.increment_year()
world.increment_year()
world.increment_year()
world.increment_year()

