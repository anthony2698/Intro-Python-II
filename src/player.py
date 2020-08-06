# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    def move(self, direction):
        if bool(getattr(self.current_room, f"{direction}_to")):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print('\nThere is nothing in that direction..\n')

