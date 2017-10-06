animals = ['dog', 'donkey', 'bird', 'cat']

def convert_list_to_string(my_list):
    my_list[-1] = 'and ' + my_list[-1]
    return ', '.join(my_list)

print(convert_list_to_string(animals))