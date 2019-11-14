from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'North',
                     [Item('mat', 'carpet'), Item('bell', 'alert on arrival')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'North-East',
                     [Item('guitar', 'musical instrument'), Item('sofa', 'comfort')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'North',
                     [Item('knife', 'sharp edge'), Item('kettle', 'boil water')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'West', [Item('keys', 'drive cars'), Item('fan', 'cools room')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'East', [Item('refrigerator', 'fridge'), Item('laptop', 'Work tool')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Joe', 45, room['outside'], [Item('bag', 'carrier bag')])


print(player1)

# Move method


def get_items(room, tools):
    output = ""
    output += "Items in room" + "\n"
    i = 1
    for c in tools:
        output += "  " + str(i) + ". " + str(c) + "\n"
        i += 1
    # add an exit message
    # output += "  " + str(i) + ". Exit"
    return output


def get_inventory(tools):
    output = ""
    output += "Items in players inventory" + "\n"
    i = 1
    for c in tools:
        output += "  " + str(i) + ". " + str(c) + "\n"
        i += 1
    # add an exit message
    # output += "  " + str(i) + ". Exit"
    return output


def move(atr, location):
    coord = atr+"_to"
    if hasattr(location, coord):
        location = getattr(location, coord)
        return location
    else:
        print('You shall not pass')


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
done = True


while done:
    print('==current room==', player1.current_room)
    if player1.current_room != None:
        print('==room description==', player1.current_room.description)
    else:
        print('ROAD IS SHUT')

    s = input("Command> ").lower().split()

    if s[0] == 'q':
        done = False
    elif s[0] in ['n', 's', 'e', 'w']:
        player1.current_room = move(s[0], player1.current_room)
    elif s[0] == 't':
     print('==room items==', get_items(
            player1.current_room, player1.current_room.items))
    elif s[0] == 'i':
        print('==player inventory==', get_inventory(player1.items))
    elif s[0] and s[1]:
        action, item = s[0], s[1]
        # print('$$$', "".join(player1.current_room.items.split(",")).split())
        print(item, '$$', player1.current_room.items)
        if action == 'get' or action == 'take':
            if player1.current_room.item_exist(item):
                removed_item = player1.current_room.remove_item(item)
                player1.add_item(item)
            else:
                print('Item does not exist')

        if action == 'drop':
            if item in player1.items:
                removed_item = player1.remove_item(item)
                player1.current_room.add_item(item)
            else:
                print('Item is not in players invemtory')
