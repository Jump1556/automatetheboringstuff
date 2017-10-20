#! /usr/bin/env python3
# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) +'.zip'
        if not os.path.exists(zip_filename):
            break
        number = number +1
    print('Creating %s...' % (zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')

backup_to_zip('/Users/anastasia/osmakedir folder')