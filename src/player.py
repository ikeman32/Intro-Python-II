# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, direction):
        '''
        Appends the cardinal direction with _to
        i.e. n_to which eliminates the need for these
        attributes to be added to the Room class.
        '''
        return getattr(self.location, f'{direction}_to')


