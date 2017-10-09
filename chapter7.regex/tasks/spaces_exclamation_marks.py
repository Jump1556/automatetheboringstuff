#! /usr/bin/env python3.
# spaces_exclamation_marks.py - Find multiple spaces between words, accidentally repeated words,
# or multiple exclamation marks.
import re, pyperclip


pyperclip.copy('ometimes  you  you may need to use the!!   matched text text itself as part of!!! the substitution')
text = str(pyperclip.paste())

multi_spaces_pattern = re.compile(r'\s{2,}')
text = multi_spaces_pattern.sub(r' ', text)
exclamation_mark = re.compile(r'!{2,}')
text = exclamation_mark.sub(r'!', text)
text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)    #remove duplicated words in row

print(text)

