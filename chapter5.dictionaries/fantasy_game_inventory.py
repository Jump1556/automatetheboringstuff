#Fantasy Game Inventory

inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def display_inventory(my_dict):
    print('Inventory:')
    for k, v in my_dict.items():
        print(v, k)
    print("Total number of items: " + str(sum(my_dict.values())))
#print(display_inventory(inventory))


#List to Dictionary Function for Fantasy Game Inventory

def add_to_inventory(my_dict, added_items):
  for i in added_items:
    my_dict.setdefault(i, 0)
    my_dict[i] = my_dict[i] + 1
  return my_dict

inv = {'gold coin':42, 'rope':1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)
print(display_inventory(inv))