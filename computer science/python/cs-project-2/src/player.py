# Write a class to hold player information, e.g. what room they are in
# currently.
# create a player item and some items to pick up
# then create a room and add the player to the room

# import rooms for composition fields
# from room import Room
from item import Item


class Player:
    def __init__(self, name, age, current_room, items):
        self.name = name
        self.age = age
        self.current_room = current_room
        self.items = items

        # methods

        # getters
    def get_name(self):
        return self.name

        # setters
    def set_name(self, name):
        self.name = name

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        new_items = []

        for item in self.items:
            if item.name.lower() == item_name:
                removed_item = item
            else:
                new_items.append(item)

            self.items = new_items
            return removed_item

    # def __str__(self):
    #     return f"Player {self.name} aged {self.age} is in {self.current_room} room. {self.item}"

    def __repr__(self):
        return f"{self.name}, {self.current_room}, {self.items}"


# s = Player('Tom', 23, 'Eko', 'Phone')
# print(s)
