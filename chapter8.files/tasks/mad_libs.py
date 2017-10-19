#! /usr/bin/env python3
#mad_libs.py - reads text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


file = open('madlib.txt', 'r')

filedata = file.read()

adjective = input("Enter an adjective:")

filedata = filedata.replace('ADJECTIVE', adjective)

noun = input("Enter a noun:")

filedata = filedata.replace('NOUN', noun, 1)

verb = input("Enter a verb:")

filedata = filedata.replace('VERB', verb)

noun = input("Enter a noun:")

filedata = filedata.replace('NOUN', noun, 1)

file = open('madlib_new.txt', 'w')
file.write(filedata)

file.close()

print_madlibs_new = open('madlib_new.txt')
content = print_madlibs_new.read()
print(content)
print_madlibs_new.close()