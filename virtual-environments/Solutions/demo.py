# Documentation at https://pypi.org/project/playsound/
# To install:
## pip install playsound

import os
from playsound import playsound

def abs_path(rel_path):
    mypath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(mypath, rel_path)

sounds = [ # All files from https://freesound.org/
    'agle17.mp3',
    'jalastram.mp3',
    'moca.mp3',
    'spennnyyy.mp3',
    'tesabob2001.mp3',
    'yay.mp3'
]

for sound in sounds:
    playsound(abs_path('sounds/' + sound))