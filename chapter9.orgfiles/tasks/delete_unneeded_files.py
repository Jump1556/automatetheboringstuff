#! /usr/bin/env python3
#delete_unneeded_files.py - program walk through a folder tree,
#search for files more than 100MB and print files names and their absolute path


import os

path = '/Users/anastasia/osmakedir folder'

for foldername, subfolders, filenames in os.walk(path):
         for filename in filenames:
             if int(os.path.getsize(foldername + '/' + filename)) > 104857600:
                 print(os.path.abspath(foldername + '/' + filename))
