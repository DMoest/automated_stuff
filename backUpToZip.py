#! python3
# backUpToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import zipfile
import pyperclip

folderClipboardPath = str(pyperclip.paste())

print(f'Start backup from the folder "{folderClipboardPath}" into a zip file.')

def backupToZip(folder):
    # Back up the entire contents of "folder" into ZIP file.
    folder = os.path.abspath(folder)  # Make sure folder is absolute.
    number = 1

    # Figure out what filename this code should use based on
    # what files already exist.
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break       # Breaks the loop if name does not exist, name can be used.
        number += 1

    # Create ZIP file
    print(f'Creating file {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)  # Add the current folder to the zip file.

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'

            # don't backup the backup zip files!
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

# Function execution on the folder path from clipboard.
backupToZip(folderClipboardPath)
