import sys
sys.path.append("../")
from quiz_functions import create_textinputquiz_widget, create_multipleChoice_widget

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

s = pd.read_csv('quiz1-nums.txt', squeeze=True, header=None, dtype=int)
s.index = ['AAH','AAL','AAS','ABA','ABS','ABY','ACE','ACT','ADD','ADO','ADS',
           'ADZ','AFF','AFT','AGA','AGE','AGO','AHA','AHI','AHS','AID','AIL',
           'AIM','AIN','AIR','AIS','AIT','ALA','ALB','ALE','ALL','ALP','ALS',
           'ALT','AMA','AMI','AMP','AMU','ANA','AND','ANE','ANI','ANT','ANY',
           'APE','APP','APT','ARB','ARC','ARE','ARF','ARK','ARM','ARS','ART',
           'ASH','ASK','ASP','ATE','ATT','AUK','AVA','AVE','AVO','AWA','AWE',
           'AWL','AWN','AXE','AYE','AYS','AZO','BAA','BAD','BAG','BAH','BAL',
           'BAM','BAN','BAP','BAR','BAS','BAT','BAY','BED','BEE','BEG','BEL',
           'BEN','BET','BEY','BIB','BID','BIG','BIN','BIO','BIS','BIT','BIZ',
           'BOA','BOB','BOD','BOG','BOO','BOP','BOS','BOT','BOW','BOX','BOY',
           'BRA','BRO','BRR','BUB','BUD','BUG','BUM','BUN','BUR','BUS']


qs = [
    ('How many elements are in the <code>s</code> Series?', '120', ''),
    ('What is the value of the first element?', '-30083', ''),
    ('What is the value of the last element?', '-4563', ''),
    ('What is the value of the 3rd to last element?', '720', ''),
    ('What is the value of the element with label "ADS"?', '-31363', ''),
    ('What is the value of the element with label "BAA"?', '-1470', ''),
    ('What is the index label of the last element?', 'BUS', ''),
]

questions = [
    create_textinputquiz_widget('<h4 style="color:darkblue">' + q[0] + '</h4>', 'Answer:', q[1], '', q[2])
    for q in qs
]


q1 = questions[0]
q2 = questions[1]
q3 = questions[2]
q4 = questions[3]
q5 = questions[4]
q6 = questions[5]
q7 = questions[6]
q8 = create_multipleChoice_widget(
    '<h4 style="color:darkblue">Are there any <code>NaN</code> values in the <code>s</code> Series?</h4>',
    ['Yes', 'No'], 'No', 'Remember the <code>any()</code> method.')