from api.models import Room
import random

room_titles = [
    "Outside Cave Entrance",
    "Plain Garden Thicket",
    "Puny Sumac Thicket",
    "Gorgeous Forest",
    "Mighty Woods",
    "Prairie Beaver Covert",
    "Tundra Hummingbird Grove",
    "Nottingfair Woods",
    "Ridgenora Thicket",
    "Hillpar Grove",
    "Falneau Wilds",
    "Magical Ironwood Wood",
    "Shaggy Loch Woods",
    "Terrible Woodland",
    "Glorious Woods",
    "Regal Swallow Timberland",
    "Black Gerbil Woodland",
    "Leamingman Timberland",
    "Pastara Covert",
    "Hadstall Covert",
    "Galcona Woods",
    "Fabulous Thorn Forest",
    "Moldy Chestnut Woodland",
    "Wicked Grove",
    "Triangular Woods",
    "Alpine Gorilla Forest",
    "Camp Foster",
    "Camp Company",
    "Camp Glory",
    "Camp Hallow",
    "Camp Venom",
    "Camp Carnage",
    "Camp Jester",
    "Camp Anomaly",
    "Camp Enigma",
    "Camp Quicksilver",
    "Grass Crab Woods",
    "Boothbron Covert",
    "Churchnola Wood",
    "Plymrose Covert",
    "Barkmar Wood",
    "Gigantic Bluff Woods",
    "Secret Beech Woods",
    "Teeny Woods",
    "Misty Timberland",
    "White Turtle Covert",
    "Long-tailed Ocelot Covert",
    "Innisdover Woods",
    "Brironto Timberland",
    "Godejour Wood",
    "Irriwin Timberland,",
    "Broad Walnut Woods",
    "Broad Ironwood Wilds",
    "Mammoth Timberland",
    "Wise Grove",
    "Rusty Sloth Woods",
    "Speckled Eagle Timberland",
    "Cheltara Covert",
    "Hfway Woods",
    "Marlfail Wilds",
    "Midadows Grove,",
    "Magical Beech Wood",
    "Huge Willow Thicket",
    "Wicked Forest",
    "Wretched Grove",
    "Masked Hedgehog Forest",
    "Spotted Turtle Grove",
    "Chamstall Wood",
    "Holylam Wood",
    "Farmingning Grove",
    "Esster Covert",
    "Sickly Fir Grove",
    "Glistening Beech Forest",
    "Lively Wood",
    "Jagged Woods",
    "Ivory Gerbil Forest",
    "Southern Mole Thicket",
    "Morinlodge Woodland",
    "Kirmeny Grove",
    "Milllodge Forest",
    "Garjour Wood",
    "Fantastic Chestnut Woods",
    "Fabulous Juniper Forest",
    "Special Woodland",
    "Teeny Wood",
    "Noble Snail Grove",
    "Royal Deer Grove",
    "Marlrood Wood",
    "Morinbo Woodland",
    "Danfolk Timberland",
    "Torringdeen Grove",
    "Gentle Elm Forest",
    "Colossal Basin Forest",
    "Wretched Wood",
    "Heavenly Thicket",
    "Maned Lion Grove",
    "Giant Leopard Wood",
    "Ridgefair Woodland",
    "Kirshire Timberland",
    "Trisby Covert",
    "Comburn Grove",
    "Threatening Hickory Timberland",
    "Minor Blackberry Timberland",
    "Square Timberland",
    "Parallel Grove",
    "Short-tailed Lion Grove",
    "Rusty Jackal Timberland",
    "Barringmeda Forest",
    "Lunending Grove",
    "Neuwall Covert",
    "Faltane Timberland",
    "Regular Pecan Forest",
    "Heavenly Blackberry Woodland",
    "Romantic Woodland",
    "Elegant Timberland",
    "Golden Mouse Wood",
    "Maned Rat Wilds",
    "Keellow Thicket",
    "Colirath Grove",
    "Canofail Grove",
    "Petrodown Woodland",
    "Ancient Butternut Thicket",
    "Huge Redwood Wilds",
    "Faint Covert",
    "Precious Woodland",
    "Collared Hyena Timberland",
    "Brown Bear Timberland",
    "Stanster Covert",
    "Brostawa Wood",
    "Berksend Woodland",
    "Livercroft Wood",
    "kurin Empire",
    "kado Empire",
    "ivista Dynasty",
    "matha Dynasty",
    "wreantis Empire",
    "vraisruzia Empire",
    "yapreral Kingdom",
    "aecazekar Dynasty",
    "emeacaseon Dynasty",
    "staregia Dynasty",
    "saisha Empire",
    "nulum Kingdom",
    "sodor Empire",
    "breoterra Kingdom",
    "hukha Dynasty",
    "ozaggicaea Kingdom",
    "uquikkolan Dynasty",
    "daemathia Kingdom",
    "anitera Kingdom",
    "duidrista Dynasty",
    "thairis Dynasty",
    "grerenth Empire",
    "goryn Dynasty",
    "beozia Empire",
    "egrerene Empire",
    "vreyivell Dynasty",
    "khosailon Empire",
    "phucceborg Kingdom",
    "stagimid Empire",
    "yayales Empire",
    "aewrebet Dynasty",
    "drurenth Dynasty",
    "lenao Empire",
    "cuidian Kingdom",
    "shoupia Dynasty",
    "qebaedo Empire",
    "payonait Kingdom",
    "qeayenem Empire",
    "abururus Kingdom",
    "hiffutopia Kingdom",
    "uyurith Dynasty",
    "xaca Dynasty",
    "pudel Dynasty",
    "marean Empire",
    "diba Empire",
    "graiyenate Kingdom",
    "slesirian Kingdom",
    "ohakrania Empire",
    "sezriteron Dynasty",
    "chibbuneian Empire",
    "xeogia Empire",
    "icisea Empire",
    "reles Dynasty",
    "saedour Kingdom",
    "vilum Kingdom",
    "supido Kingdom",
    "istotaning Dynasty",
    "acruxaca Kingdom",
    "apikrenyth Empire",
    "shafantis Dynasty",
    "daterra Dynasty",
    "ounarene Dynasty",
    "vrigon Kingdom",
    "titha Dynasty",
    "odeaniel Dynasty",
    "bevales Kingdom",
    "haebentis Empire",
    "ikhepuidora Dynasty",
    "evruitidel Kingdom",
    "eaxecivell Dynasty",
    "uzinait Dynasty",
    "shibia Empire",
    "sleaniel Dynasty",
    "moria Kingdom",
    "slubet Empire",
    "sleochasan Empire",
    "aewregoutish Empire",
    "theokotor Dynasty",
    "hodeanate Dynasty",
    "alallokar Dynasty",
    "Nascombe Keep",
    "Waelmore Hold",
    "Sella Hold",
    "Ryre Keep",
    "Kalepeck Castle",
    "Miserth Fort",
    "Ranhold Citadel",
    "Fangdor Fortress",
    "Parthley Hold",
    "Baston Castle",
    "Cannersly Castle",
    "Starnborough Stronghold",
    "Lorton Palace",
    "Middleborough Stronghold",
    "Eynsworth Fort",
    "Karthmere Fort",
    "Moldermouth Hold",
    "Lardel Citadel",
    "Haeresceugh Citadel",
    "Streganna Hold",
    "Startlam Fort",
    "Bellbroke Citadel",
    "Borthrough Hold",
    "Darnstall Hold",
    "Malgrave Stronghold",
    "Caenleigh Stronghold",
    "Harlston Hold",
    "Chastershire Fortress",
    "Bartham Hold",
    "Dustorn Keep",
    "Windsor Palace",
    "Coarshire Keep",
    "Curlisbrooke Hold",
    "Shardore Fort",
    "Tharnham Stronghold",
    "West Lowes Keep",
    "Elden Castle",
    "Summerswind Palace",
    "Bargsea Citadel",
    "Moldermouth Palace",
    "Alnor Palace",
    "Cullin Fort",
    "Haword Fortress",
    "Tessaway Hold",
    "Tharnham Keep",
    "Arcop Fortress",
    "Caenleigh Fortress",
    "Ormshire Fort",
    "Yielden Hold",
    "Naesbrey Citadel",
    "Kentillie Citadel",
    "Rundhey Palace",
    "Mirador Castle",
    "Wulworth Hold",
    "Moldermouth Stronghold",
    "Angarth Citadel",
    "Fernyard Stronghold",
    "Draydon Keep",
    "Eldford Fort",
    "Zatherop Fortress",
    "Calbridge Hold",
    "Elden Fortress",
    "Longdale Citadel",
    "Yorthendon Castle",
    "Witton Castle",
    "Broadborough Hold",
    "Howlester Fortress",
    "Whitich Fort",
    "Barviel Citadel",
    "Goodmond Castle",
    "Skelside Palace",
    "Haeresceugh Keep",
    "Carby Palace",
    "Queensborough Keep",
    "Langen Keep",
    "Wilton Citadel",
    "Bacre Fortress",
    "Hingham Fortress",
    "Stowerling Hold",
    "Almerry Castle",
    "Chilgrave Stronghold",
    "Starm Stronghold",
    "Wray Castle",
    "Cladborough Citadel",
    "Ryre Castle",
    "Capvering Keep",
    "Ely Citadel",
    "Otterberg Stronghold",
    "Merryport Citadel",
    "Stormholme Palace",
    "Dragonspire Castle",
    "Windkeep Fort",
    "Yielden Hold",
    "Dorgoil Palace",
    "Narlington Keep",
    "Barviel Castle",
    "Gourdley Keep",
    "Haersley Keep",
    "Elden Castle",
    "Goulrich Stronghold",
    "Cublerton Fort",
    "Highcalere Castle",
    "Bruckstone Fort",
    "Darthill Hold",
    "Wardford Citadel",
    "Kaerndal Castle",
    "Cadleigh Fort",
    "Blaise Palace",
    "Lamberside Citadel",
    "Goodmond Citadel",
    "Ultrona Castle",
    "Candor Fortress",
    "Shaldorn Stronghold",
    "Brawnlyn Keep",
    "Hopeshire Fortress",
    "Carneath Fortress",
    "Ormshire Castle",
    "Staerdale Citadel",
    "Cadleigh Keep",
    "Faemley Castle",
    "Langen Castle",
    "Termarth Keep",
    "Bourgh Citadel",
    "Carneath Castle",
    "Breuce Citadel",
    "Grimtol Fortress",
    "Heathersage Fortress",
    "Darthill Hold",
    "Fanthorpe Fort",
    "Custaeton Palace",
    "Highcalere Keep",
    "Aebarrow Palace",
    "Starm Palace",
    "Starkport Stronghold",
    "Croftvalley Fortress",
    "Treehold Fort",
    "Waerlden Keep",
    "Arpton Fort",
    "Chastershire Citadel",
    "Wardhurst Fortress",
    "Curlisbrooke Hold",
    "Clarn Hold",
    "Eastormel Fort",
    "Gatterlen Castle",
    "Cladborough Fort",
    "Miserth Keep",
    "Headdon Citadel",
    "Larton Stronghold",
    "Withall Stronghold",
    "Parverhill Keep",
    "Windmontley Stronghold",
    "Lamberside Fortress",
    "Alderth Fort",
    "Gundor Stronghold",
    "Stowe Fort",
    "Kirkoswald Castle",
    "Croilton Stronghold",
    "Whitstone Hold",
    "Whitstone Citadel",
    "Sella Stronghold",
    "Flamewing Guard",
    "Narrowmount Refuge",
    "Valorclaw Outpost",
    "Witherrock Stronghold",
    "Fargrasp Point",
    "Phantom Point",
    "Mountain Guard",
    "Fool Hope Headquarters",
    "Crystal Guard",
    "Scarlet Guard",
    "Whitewater Bulwark",
    "Shadestorm Garrison",
    "Coldshire Bulwark",
    "Sabregrip Fortification",
    "Rubblelanding Hold",
    "Camp Conquest",
    "Camp Revolution",
    "Camp Tribute",
    "Camp Torment",
    "Camp Slaughter",
    "Camp Agony",
    "Camp Lockdown",
    "Camp Mountain Peak",
    "Camp Boulderfist",
    "Camp Firefly",
    "Lake Terminal",
    "Canyon Outpost",
    "Obsidian Harbor",
    "Autumn Command",
    "Spring Redoubt",
    "Swampbranch Camp",
    "Goldblossom Barracks",
    "Swiftwood Stand",
    "Dustspire Command",
    "Flamelord Stronghold",
    "Twilight Stronghold",
    "Falcon Frontier",
    "Sleeping Stronghold",
    "Mountain Wall",
    "Burning Fortification",
    "Summermore Post",
    "Direwharf Point",
    "Flamedrift Station",
    "Fogland Castle",
    "Rivertalon Guard",
    "Terror Site",
    "Raven Citadel",
    "Talon Front",
    "Vendetta Depot",
    "Valley Stronghold",
]


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):

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
        # set to 1 so id can begin at 1
        room_count = 1

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None

        # use to reverse the direction of the room
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e", "err": "err"}

        # will be used to create chasm
        break_choices = [False, True, False, False, False]

        while room_count <= num_rooms:

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
                # set the direction to something useless
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
            room = Room(id=room_count, title=room_titles[room_count - 1],
                        description="The quest for thy nobly ring burns true and bright. Search on thou famed voyager!", x=x, y=y)
            # Note that in Django, you'll need to save the room after you create it
            room.save()

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_dirs[room_direction])

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
                    self.grid[y][x].connectRooms(self.grid[y + 1][x], "n")
                    self.grid[y + 1][x].connectRooms(self.grid[y][x], "s")

            # increment x
            x += 1
            # increment room_count
            room_count += 1

            # if x is at the last position increment y and reset x
            if x == size_x:
                x = 0
                y += 1

    def print_rooms(self):

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
                if room != 0 and room.n_to != 0:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room != 0 and room.w_to != 0:
                    str += "-"
                else:
                    str += " "
                if room != 0:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room != 0 and room.e_to != 0:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room != 0 and room.s_to != 0:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)
