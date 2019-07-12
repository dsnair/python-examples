# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return self.current_room

    def take_item(self, *args):
        self.items.extend(list(args))