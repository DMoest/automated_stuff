# python3

import shutil
import os
import re
import sys
import pyperclip


if len(sys.argv) > 1:
    directory = str(sys.argv[1:])
else:
    directory = str(pyperclip.paste())

thePatterns = re.compile(r"""
    ([_]+)         # Characters to replace.
    """, re.VERBOSE)
    # ([...]+)       # Characters to replace.

print(f'Listing files in directory {directory}... ')
for theFileName in os.listdir(directory):
    mo = thePatterns.search(theFileName)

    if mo is None:
        continue
    else:
        # replace characters in string
        newFileName = theFileName.replace("_", " ")
        # newFileName = theFileName.replace("...", "")    # Remove excessive dots.

        # Get the full, absolute file path.
        absWorkingDir = os.path.abspath(directory)
        theFileName = os.path.join(absWorkingDir, theFileName)
        newFilename = os.path.join(absWorkingDir, newFileName)

        print(f'Renaming "{theFileName}" to "{newFileName}" ')
        shutil.move(theFileName, newFileName) # Uncomment after testing.
