#! /usr/bin/env python3
#filling_gaps.py - finds all files with a given prefix and locates any gaps in the numbering,
# renames all the later files to close this gap.


import os, shutil


folder = input('Provide folder: ')
prefix = input('Provide prefix: ')
filenames = []

for filename in os.listdir(folder):
    if filename.startswith(prefix):
        filenames.append(filename)
print('List of files in the folder: ' + str(filenames))


index = 0

for filename in filenames:
    index += 1
    new_filename = prefix + str('%02d' % index) +'.txt'
    if filename == new_filename:
        continue
    else:
        shutil.move((folder + filename), (folder + new_filename))
        print('File ' + filename + ' renamed to file ' + new_filename)



