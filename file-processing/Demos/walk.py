import os
from pathlib import Path

def spaces2dashes():
    for dirpath, dirnames, filenames in os.walk('my_files'):
        for fname in filenames:
            if ' ' in fname:
                oldname = Path(dirpath) / fname
                newname = Path(dirpath) / fname.replace(' ', '-')
                print("Replacing", oldname.name, "with", newname.name)
                oldname.rename(newname)

def dashes2spaces():
    for dirpath, dirnames, filenames in os.walk('my_files'):
        for fname in filenames:
            if '-' in fname:
                oldname = Path(dirpath) / fname
                newname = Path(dirpath) / fname.replace('-', ' ')
                print("Replacing", oldname.name, "with", newname.name)
                oldname.rename(newname)

spaces2dashes()