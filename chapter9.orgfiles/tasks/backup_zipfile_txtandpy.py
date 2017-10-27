#! /usr/bin/env python3
# backup_zip_txtandpy.py - Walk a directory tree and archive just files with certain extensions
# such as .txt or .py, and nothing else

import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)
    for filename in os.listdir(folder):
        if filename.endswith('.txt') or filename.endswith('.py'):
            while True:
                zip_filename = os.path.basename(folder) + '.zip'
                if not os.path.exists(zip_filename):
                    break
            print('Creating %s...' % (zip_filename))
            backup_zip = zipfile.ZipFile(zip_filename, 'w')

            for foldername, subfolders, filenames in os.walk(folder):
                print('Adding files in %s...' % (foldername))
                backup_zip.write(foldername)
                for filename in filenames:
                    new_base = os.path.basename(folder)
                    if filename.startswith(new_base) and filename.endswith('.zip'):
                        continue
                    backup_zip.write(os.path.join(foldername, filename))
            backup_zip.close()
            print('Done.')

