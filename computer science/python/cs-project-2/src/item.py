"""
Create a file called item.py and add an Item class in there.

The item should have name and description attributes.

Hint: the name should be one word for ease in parsing later.
This will be the base class for specialized item types to be declared later.
"""


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def __str__(self):
    #     return f'List of items {self.name} and their descriptions {self.description}'

    def __repr__(self):
        return f'{self.name}, {self.description}'


# item1 = Item('ps4', 'game console')
