#! /usr/bin/env python3.
# strong_pw_detector.py - Check if the password string is strong enough.
import re


upper_reg = re.compile(r'.*[A-Z].*')
lower_reg = re.compile(r'.*[a-z].*')
digit_reg = re.compile(r'.*[0-9].*')

def strong_pw_detector(password):
    if len(password) >= 8:
        if upper_reg.search(password) and lower_reg.search(password) and digit_reg.search(password):
            print('It is strong password')
        else:
            print("Strong password contains upper and lowercase letters as well as digit.")
    else:
        print("Strong password contains at least 8 characters.")


print(strong_pw_detector('ffff9907H'))
