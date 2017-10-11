#! /usr/bin/env python3.
# find_urls.py - Find website URLs that begin with http:// or https://.
import re, pyperclip


pyperclip.copy('is my tweet check it out http://tinyurl.com/blah and https://blabla.com')
text = str(pyperclip.paste())

match = re.findall(r'(https?://\S+)', text)
print(match)
