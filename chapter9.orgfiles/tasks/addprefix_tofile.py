#! /usr/bin/env python3
#addprefix_tofile.py - adds a prefix to the start of the filename


import os, shutil

def find_all_txt (mydir):
    for filename in os.listdir(mydir):
        if filename.endswith(".txt"):
            new_filename = 'new'+filename
            shutil.move(str(mydir +'/' +filename), str(mydir +'/' +new_filename))

print(find_all_txt('/Users/anastasia'))
