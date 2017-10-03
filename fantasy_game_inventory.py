inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def display_inventory(my_dict):
    print('Inventory:')
    for k, v in my_dict.items():
        print(v, k)
    print("Total number of items: " + str(sum(my_dict.values())))

print(display_inventory(inventory))
