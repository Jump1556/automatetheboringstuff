#! /usr/bin/env python3.
# table_printer.py - function to display table in a well-organized way
# with each column right-justified based on longest string inside lists.

def print_table(my_list):
    colWidths = [0] * len(my_list)
    i = 0
    for lines in my_list:
        for word in lines:
            str_len = len(word)
            if str_len > colWidths[i]:
                colWidths[i]=str_len
        i += 1

    for i in range(len(my_list[0])):
        for j in range(len(my_list)):
            print(my_list[j][i].rjust(colWidths[j]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)