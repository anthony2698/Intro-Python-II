# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.n_to = self.s_to = self.e_to = self.w_to = None
        self.description = description
    def __str__(self):
        return f"\nYou are currently {self.name}, {self.description}!\n"