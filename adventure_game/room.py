# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # static variables
    n_to = None
    s_to = None
    w_to = None
    e_to = None

    # instantiate objects
    # allows calling Room.name & Room.description
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_item(self, *args):
        self.items = args