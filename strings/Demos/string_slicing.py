phrase = "Monty Python"

first_5_letters = phrase[0:5] # [Monty] Python
print(first_5_letters)

letters_2_thru_4 = phrase[1:4] # M[ont]y Python
print(letters_2_thru_4)

letter_5_to_end = phrase[4:] # Mont[y Python]
print(letter_5_to_end)

last_3_letters = phrase[-3:] # Monty Pyt[hon]
print(last_3_letters)

first_3_letters = phrase[:3] # [Mon]ty Python
print(first_3_letters)

three_letters_before_last = phrase[-4:-1] # Monty Py[tho]n
print(three_letters_before_last)

copy_of_string = phrase[:] # [Monty Python]
print(copy_of_string)