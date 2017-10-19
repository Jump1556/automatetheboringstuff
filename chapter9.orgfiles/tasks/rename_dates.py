#! /usr/bin/env python3
#rename_dates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.


import re, os, shutil

us_date = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-              # one or two digits for the month
       ((0|1|2|3)?\d)-          # one or two digits for the day
       ((19|20)\d\d)            # four digits for the year
       (.*?)$                   # all text after the date
       """, re.VERBOSE)

for usFilename in os.listdir('.'):
    match = us_date.search(usFilename)
    if match == None:
        continue
    before_part = match.group(1)
    month_part = match.group(2)
    day_part = match.group(4)
    year_part = match.group(6)
    after_part = match.group(8)

    euFilename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    abs_workdir = os.path.abspath('.')
    usFilename = os.path.join(abs_workdir, usFilename)
    euFilename = os.path.join(abs_workdir, euFilename)

shutil.move(usFilename, euFilename)