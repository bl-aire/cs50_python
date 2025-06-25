# CLASS METHOD
# we do not want to instantiate hat or have multiple instances of Hat
# we won't need __init__ or sort method here

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")