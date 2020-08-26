# EXAMPLE 1: Breaking method arguments across multiple lines
phrase = ("On a scale of {} to {}, I give {} a {}.".format(1, 5,
                                                           "Monty Python", 6))
print(phrase)

location = "ponds"
items = "swords"
beings = "masses"
adjective = "farcical"

# EXAMPLE 2: Concatenation
quote = ("Listen, strange women lyin' in {} " +
         "distributin' {} is no basis for a system of " +
         "government. Supreme executive power derives from " +
         "a mandate from the {}, not from some {} " +
         "aquatic ceremony.").format(location, items,
                                     beings, adjective)

print(quote)

# EXAMPLE 3: Triple quotes
quote = """Listen, strange women lyin' in {} \
distributin' {} is no basis for a system of \
government. Supreme executive power derives from \
a mandate from the {}, not from some {} \
aquatic ceremony.""".format(location, items,
                            beings, adjective)

print(quote)