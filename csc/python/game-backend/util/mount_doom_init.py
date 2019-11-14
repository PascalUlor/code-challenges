from util.world import World
from api.models import Player

w = World()
num_rooms = 400
width = 20
height = 20
w.generate_rooms(width, height, num_rooms)
w.print_rooms()

players = Player.objects.all()

for p in players:
    # set the current room to the first room
    p.currentRoom = 1
    p.save()
