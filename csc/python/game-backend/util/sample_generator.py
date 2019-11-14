# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

import random
from rooms import room_titles


class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"

        return f"({self.x}, {self.y})"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''

        # add a key err for bad mapping
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e", "err": "err"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid's height
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y

        # fill the row up with an array of None
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None

        # will be used to create chasm
        break_choices = [False, True, False, False, False]

        while room_count < num_rooms:
            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # REMOVED THE NORTH SOUTH MAPPING AT THE ENDS OF THE MAP
                # # If we hit a wall, turn north and reverse direction
                # set a direction err for no mapping
                room_direction = "err"
                y += 1
                direction *= -1

            # THIS CREATES A CHASM IN THE EAST-WEST CONNECTION AT RANDOM POINTS
            # if 1 < y < (size_y - 3)
            if 1 < y < (size_y - 3):
                # randomize break_choices
                choice = random.choice(break_choices)
                # if true break the connection by setting the room direction to err
                if choice:
                    room_direction = "err"

            # Create a room in the given direction
            room = Room(room_count, room_titles[room_count],
                        "The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", x, y)
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1

        # THIS STEP DOWNWARD WILL CREATE NORTH-SOUTH CONNECTIONS AT RANDOM POINTS IN THE MAP
        # set room_count to zero again
        room_count = 0
        # set x and y to zero
        x = 0
        y = 0
        # set another variable index to zero
        # create an array range to hold choices
        choices = [False, True, False, False, True]
        # loop while room_count is less than num_rooms
        while room_count < num_rooms:
            # if y is less than size_y
            if y < size_y - 1:
                # randomize choices
                # if true set a northward position
                if random.choice(choices):
                    # connect with the room to the north
                    self.grid[y][x].connect_rooms(self.grid[y + 1][x], "n")

            # increment x
            x += 1
            # increment room_count
            room_count += 1

            # if x is at the last position increment y and reset x
            if x == size_x:
                x = 0
                y += 1

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 169
width = 13
height = 13
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
