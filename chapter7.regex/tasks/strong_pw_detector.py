#! /usr/bin/env python3.
# strong_pw_detector.py - Check if the password string is strong enough.
import re


def strong_pw_detector(password):
    if len(password) >= 8:
        strong_pw = re.compile(r'''(
        [a-z]+
        [A-Z]+
        [0-9]+
        )''', re.VERBOSE)
        if strong_pw.match(password):
            print('It is strong password')
        else:
            print("Strong password contains upper and lowercase letters as well as digit.")
    else:
        print("Strong password contains at least 8 characters.")


print(strong_pw_detector('HTad565865'))
