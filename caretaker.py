#!/usr/bin/env python3
import sys, os
import datetime, time
import shutil
from pathlib import Path

# Caretaker keeps your downloads folder clean
# by checking for files older than one month, 
# and then asking if you want to move it, or delete it

# Cheeky globals, but this is just a hacky script
user_root = str(Path.home())
download_dir = user_root + '/Downloads/'
doc_dir = user_root + '/Documents/'
pics_dir = user_root + '/Pictures/'
vids_dir = user_root + '/Videos/'

def get_old_files(directory):

    files = os.listdir(directory)
    epoch_month_ago = time.time() - 2678400
    old_files = []
    for f in files:
        file_created = os.path.getmtime(directory + '/' + f)
        if file_created < epoch_month_ago:
            old_files += [f]

    return old_files

def move_or_delete(fil):
    print(fil)
    in_str = 'Move file to (D)ocuments, (P)ictures, (V)ideos | (R)emove| (I)gnore\n'

    choice = input(in_str).lower()

    if choice == 'd':
        shutil.move(download_dir + f, doc_dir + f)
    elif choice == 'p':
        shutil.move(download_dir + f, pics_dir + f)
    elif choice == 'v':
        shutil.move(download_dir + f, vids_dir + f)
    elif choice == 'r':
        if os.path.isfile(download_dir + f):
            os.remove(download_dir + f)
        else:
            shutil.rmtree(download_dir + f)
    elif choice == 'i':
        print('Ignored file')
    elif choice == 'a':
        print('goodbye')
        exit()

if __name__ == '__main__':

    old_files = get_old_files(download_dir)

    if len(old_files) != 0:

        print('Found ', len(old_files), 'old files in Downloads. Would you like to proceed?')

        choice = input('(Y)es | (A)bort\n').lower()
        while (choice != 'y') and (choice != 'a'):
            choice = input('(Y)es | (A)bort\n').lower()

        if choice != 'y':
            exit()
        else:
            print('You can (A)bort at any time')
            for f in old_files:
                move_or_delete(f)
