fruits = ['apples', 'bananas', 'tofu', 'cats']

def convert_list_to_string(words_list):
    lastitem = words_list[-1]
    del words_list[-1]
    words_list.append('and ' + lastitem)
    return ', '.join(words_list)

print(convert_list_to_string(fruits))


animals = ['dog', 'donkey', 'bird', 'cat']

def take_list_return_string(my_list):
    my_list[-1] = 'and ' + my_list[-1]
    return ', '.join(my_list)

print(take_list_return_string(animals))