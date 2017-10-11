grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def print_image(my_lists):
  new_list = [[] for _ in range(6)]
  for i in range(len(my_lists[0])):
    for j in range(len(my_lists)):
      new_list[i].append(my_lists[j][i])
    print(new_list[i])

print_image(grid)

