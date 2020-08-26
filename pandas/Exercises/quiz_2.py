import sys
sys.path.append("../")
from quiz_functions import create_textinputquiz_widget

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

csv ='../csvs/nc-est2019-agesex-res.csv'
pops = pd.read_csv(csv, usecols=['SEX', 'AGE', 'POPESTIMATE2018', 'POPESTIMATE2019'])

def fix_sex(sex):
    if sex == 0:
        return 'T'
    elif sex == 1:
        return 'M'
    else: # 2
        return 'F'
    
pops.SEX = pops.SEX.apply(fix_sex)

qs = [
    ('How many males in their 30s were there in 2018?', '21943610', ''),
    ('What was the average age of all people in 2019 rounded to the nearest integer?', '39', 'Scroll to bottom.'),
]

questions = [
    create_textinputquiz_widget('<h4 style="color:darkblue">' + q[0] + '</h4>', 'Answer:', q[1], '', q[2])
    for q in qs
]

q1 = questions[0]
q2 = questions[1]