# an example program that uses the os.walk() function on the directory tree
import os

for folderName, subfolders, filenames in os.walk('/Users/anastasia/Documents'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')