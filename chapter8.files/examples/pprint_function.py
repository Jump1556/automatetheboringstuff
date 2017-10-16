# Using pprint.pformat() gives a string that you can write to .py file.
# This file will be your own module that you can import whenever you want to use
import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)       #return list as string
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')    #open file to write a string there
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

fileObj.close()

fileobj = open('myCats.py')
content = fileobj.read()
content
"cats = [{'desc': 'chubby', 'name': 'Vasya'}, {'desc': 'fluffy', 'name': 'Alisa'}]\n"


import myCats    #possibility to reuse your module
myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
'Zophie'