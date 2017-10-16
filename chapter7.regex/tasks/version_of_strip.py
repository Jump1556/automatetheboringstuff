#! /usr/bin/env python3.
# version_of_strip.py - Check if the password string is strong enough.
import re

def stripRegex(s, toStrip='' ):
    if toStrip=='':
        toStrip = '\s'
    pattern= re.compile(r'^{0}|{0}$'.format(toStrip))
    return pattern.sub('', s)

print(stripRegex("hh hgts hh", "hh "))

string = "tas"
string_new = "Ana{0}ia {1} - Valdenmaiier ".format(string, "Kostashenko")
string_new = "Anas%sia" % string
string_new = "Anas" + string + "ia"
print(string_new)
