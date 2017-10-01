grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid2 = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'j', 'k']]


def print_image(my_lists):
  #new_list=[]
  for j in range(len(my_lists)):
    for i in range(len(my_lists[j])):
      my_lists[j][i]

  return my_lists

print(print_image(grid))

#print (grid1[0]) #print 1 list
#print (grid1[0][1]) #print 1 list, 2 item
#print (grid1[2][3]) #print 3 list , 4 item