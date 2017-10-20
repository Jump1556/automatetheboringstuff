#! /usr/bin/env python3
# regex_search.py - a program that opens all .txt files in a folder
# and searches for any line that matches a user-supplied regular expression.

import os, re

user_reg = str(input("Print your regex pattern: "))
string_regex = re.compile(user_reg)

folder = '/Users/anastasia/'
for filename in os.listdir(folder):    #to find all the files in the working directory.
    if filename.endswith('.txt'):
        text_file = open(folder + filename)
        for string in text_file:
            match = re.findall(string_regex,string)
            if match:
                print(match)

