import sys
sys.path.append("../")
from quiz_functions import create_textinputquiz_widget

import numpy as np

def create_num(i):
    if i % 2 == 0:
        num = i**2 / 2
    else:
        num = -i**2 / 3
    return int(round(num,1) * 10)
    
nums = [create_num(i) for i in range(120)]
ar = np.array(nums)
ar = ar.reshape(15, 8)

qs = [
    ('How many elements are in the array?', '120', 'Arrays have a <code>size</code> property.'),
    ('How many dimensions is the array?', '2', 'Arrays have an <code>ndim</code> property.'),
    ('How many rows are in the array?', '15', 'Use <code>np.size()</code>, passing in the array and the dimension.'),
    ('How many columns are in the array?', '8', 'Use <code>np.size()</code>, passing in the array and the dimension.'),
    ('What is the sum of all the elements in the 4th row?', '4161', 'Call <code>sum()</code> on the 4th row.'),
    ('What is the sum of all the elements in the 5th column?', '359600', 'Call <code>sum()</code> on the 5th column.'),
    ('What is the value in the 4th column of the 5th row?', '-4083', 'Use slicing.'),
    ('What is highest value in the array?', '69620', 'Arrays have a <code>max()</code> method.'),
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
q8 = questions[7]