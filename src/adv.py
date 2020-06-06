from room import Room
from player import Player
from helpers import sys_clear as cls  # For clearing the screen
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.

"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.

"""),

    'death': Room("Dead", """For reasons known only to you, you have 
leapt over the edge into the darkend abyss. Only the fleeting remnants of your echoing
voice as you scream is all that remain of your existence

"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.

"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.

"""),
}

room['foyer'].items.append(Item('a sword', '''A one-handed sword'''))
room['overlook'].items.append(Item('a map', '''A map showing the location of the treasure room.
    From the Foyer go east to Narrow Passage then go north the Treasure room is there.'''))
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].n_to = room['death']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
cls()

player = Player(input('Please give your Player a name: '), room['outside'])

movements = '''To move press n for north, e for east, s for south or w for west. 
Type look to have a look around.
Type take to pick up any items in the room.
Type drop any item you may be carrying.
Press i to list the items in you inventory.
To quit press q.

'''

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

playing_game = True

cls()
print(movements)

print(
    f'Welcome {player.name} you are currently at an {player.location.name} \n\n')
print(f'{player.location.description}\n\n')

action = input('What do you wish to do? ')

# Changes the players location via room['name'].n_to etc.
player.location = player.move(action)

if action == 'q':
    playing_game = False

while playing_game:

    try:
        cls()

        if player.location.name != 'Dead':
            if action == 'q':  # Quite the game
                playing_game = False
            elif action == 'look':
                for item in player.location.items:
                    cls()
                    print(f'You find {item.name}, {item.description}\n')
                    print(
                        f'You are in the {player.location.name}\n\n{player.location.description}')

                action = input('What do you wish to do? ')
            elif action == 'take':
                playing_game = False
                    #print('Nothing to see')
                '''player.name.items.append(player.location.items)
                player.location.items.clear()   

                print(f'You take {player.name.items} \n')   
                print(
                f'You are in the {player.location.name}\n\n{player.location.description}')

                action = input('What do you wish to do? ')    '''

            print('\n' + movements)
            print(
                f'You are in the {player.location.name}\n\n{player.location.description}')

            action = input('What do you wish to do? ')

        else:
            print(
                f'You have fallen to your death\n\n {player.location.description}\n')

            playing_game = False

    except:  # If player enters an invalid selection
        cls()

        print(movements)
        print('You can\'t got that direction!')
        print(f'{player.location.description} \n\n')

        action = input('What do you wish to do? ')

        if action == 'q':
            playing_game = False
