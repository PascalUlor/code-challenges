car_dict = {}
new_dict = {'vegetable': 'onion', 'fruit':'apple', 'grain':'maize'}

print(new_dict['vegetable'])

car_dict['electronic'] = 'tesla'

print(car_dict)

for el in new_dict:
    print(f'{new_dict[el]} is a {el}')