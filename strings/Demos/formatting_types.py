# Full formatting strings.
sentence = 'On a scale of {0:d} to {1:d}, I give {2:s} a {3:d}.'
sentence = sentence.format(1, 5, 'Monty Python', 6)
print(sentence)

# Simplify by removing field names (indexes).
sentence = 'On a scale of {:d} to {:d}, I give {:s} a {:d}.'
sentence = sentence.format(1, 5, 'Monty Python', 6)
print(sentence)

# Further simplify by removing default type specifiers.
sentence = 'On a scale of {:} to {:}, I give {:} a {:}.'
sentence = sentence.format(1, 5, 'Monty Python', 6)
print(sentence)

# And with the field name and type specifier gone, we can
# remove the colon separator.
sentence = 'On a scale of {} to {}, I give {} a {}.'
sentence = sentence.format(1, 5, 'Monty Python', 6)
print(sentence)