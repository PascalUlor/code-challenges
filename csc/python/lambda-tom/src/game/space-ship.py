# add playing functionality
import sys
import random

# implement class to deal with the map
class Space:
# space class with rows and cols
    # constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Allocate list to hold space
        self.space = [] # rows of space

        # iterate over the rows and add cols
        for _ in range(rows):
            newRow = ["."] * cols # array of 'cols' '.'s
            # append the row to space
            self.space.append(newRow)
        
        # throw some stars in about 7% of space
        starCount = int(rows * cols * 0.07)
        # work out 7% of map

        # iterate over stars
        for _ in range(starCount):
            # random row star
            rowNum = random.randint(0, len(self.space) - 1)
            # random col star
            colNum = random.randint(0, len(self.space) - 1)
            # add the '*' to space at row and col
            self.space[rowNum][colNum] = "*"
        
        # Add the ship
        self.shipRow = rows // 2
        self.shipCol = cols // 2

        # Kill any star at the ships location
        self.space[self.shipRow][self.shipCol] = "."


    # print map function
    def printMap(self):
        # iterate over space rows
        for r in range(self.rows):
            # iterate over space cols
            for c in range(self.cols):
                # check if the ship is in the grid space
                if r == self.shipRow and c == self.shipCol:
                    # draw the ship here
                    sys.stdout.write("Y ")
                # otherwise
                else:
                    # create a symbol from data in space list
                    symbol = self.space[r][c]
                    # write the col
                    sys.stdout.write(f"{symbol} ")
            
            print()


    # move ship function
    def moveShip(self, dir):
        # hold delta X and delta Y
        dx = 0
        dy = 0

        # convert direction to delta x and delta y
        
        # if direction is "N"
        if dir == "N":
            # set delta Y to -1
            dy = -1
        # else if direction is "S"
        elif dir == "S":
            # set delta Y to 1
            dy = 1
        # else if direction is "W":
        elif dir == "W":
            # set delta X to -1
            dx = -1
        # else if direction is "E":
        elif dir == "E":
            # set delta X to 1
            dx = 1

        # increment ship col by delta x
        self.shipCol += dx
        # increment ship row by delta y
        self.shipRow += dy

        # bounds checking
    
        # if the ship to far col- set to zero
        if self.shipCol < 0:
            self.shipCol = 0
        # otherwise if ship too far col+ set to bounds - 1
        elif self.shipCol >= self.cols:
            self.shipCol = self.cols - 1

         # if the ship to far row- set to zero
        if self.shipRow < 0:
             self.shipRow = 0
        # otherwise if ship too far row+ set to bounds - 1
        elif self.shipRow >= self.rows:
            self.shipRow = self.rows - 1

# instantiate a space object
s = Space(10, 10)

# set a REPL

    # print the map
while True:
    s.printMap()
    # Take input
    d = input("Direction (N,S,E,W): ")

    # clean input
    d = d.strip().upper()

    # check for invalid input
    if d not in ["N", "S", "E", "W"]:
        continue

    # move the ship
    s.moveShip(d)

