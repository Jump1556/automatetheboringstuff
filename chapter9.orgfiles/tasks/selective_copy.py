#! /usr/bin/env python3
# selective_copy.py - a program that walks through a folder tree
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.


import os, shutil

def selective_copy(path):
    for dirname, dirnames, filenames in os.walk(path):
        print('The current folder is ' + dirname)
        new_path = (path + 'new_folder/')
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        for filename in filenames:
            path_name = dirname + '/' + filename
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy(path_name, new_path)

selective_copy()

