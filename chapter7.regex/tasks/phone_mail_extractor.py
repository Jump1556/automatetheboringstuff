#! /usr/bin/env python3.
# phone_mail_extractor.py - Finds phone numbers and email addresses on the clipboard.
import re, pyperclip


phone_regex = re.compile(r'''(
    (\d{3})                       # operator code
    (\s|-|\.)                        # separator
    (\d{3})                       # first 3 digits
    (\s|-|\.)                        # separator
    (\d{2})                       # 2 digits
    (\s|-|\.)                        # separator
    (\d{2})                       # last 2 digits
    )''', re.VERBOSE)


email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)


pyperclip.copy('''Phone: 080-420 72 40 or +1 415.863.99.00 (9 a.m. to 5 p.m., M-F, PST)
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
''')
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    matches.append(phone_num)
for groups in email_regex.findall(text):
       matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


