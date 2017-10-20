#! /usr/bin/env python3
#addprefix_tofile.py - adds a prefix to the start of the filename


import os, shutil

def find_all_txt (mydir):
    for filename in os.listdir(mydir):
        if filename.endswith(".txt"):
            print(os.path.join(mydir, filename))

print(find_all_txt('/Users/anastasia'))

# shutil.move(filename, new_name)
