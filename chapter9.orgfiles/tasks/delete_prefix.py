#! /usr/bin/env python3
#delete_prefix.py - delete prefix from the start of the filename


import os, shutil

def delete_prefix(mydir):
    for filename in os.listdir(mydir):
        if filename.endswith(".txt"):
            new_filename = filename.replace('new','')
            print(new_filename)
            shutil.move(str(mydir +'/' +filename), str(mydir +'/' +new_filename))

delete_prefix('/Users/anastasia')
