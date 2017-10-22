#! /usr/bin/env python3
# mcbextension.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcbextension.pyw save and delete <keyword> - Saves or delete clipboard to keyword.
#        py.exe mcbextension.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcbextension.pyw list - Loads all keywords to clipboard.
#        py.exe mcbextension.pyw delete - Delete all keywords.


import shelve, pyperclip, sys


mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    print(sys.argv[1])
    if sys.argv[1].lower() == 'save':
        print(sys.argv[2])
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() =='delete':
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()

mcb_shelf.close()
