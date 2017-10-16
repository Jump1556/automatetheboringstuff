#! /usr/bin/env python3.
# version_of_strip.py - Check if the password string is strong enough.
import re

def stripRegex(s, toStrip='' ):
    if toStrip=='':
        toStrip = '\s'
    pattern= re.compile(r'^{0}|{0}$'.format(toStrip))
    return pattern.sub('', s)

print(stripRegex("hh hgts hh", "hh"))
