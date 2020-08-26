ww2_leaders = [
    ('Charles', 'de Gaulle'),
    ('Winston', 'Churchill'),
    ('Teddy', 'Roosevelt'), # Not a WW2 leader, but helps illustrate the point
    ('Franklin', 'Roosevelt'),
    ('Joseph', 'Stalin'),
    ('Adolph', 'Hitler'),
    ('Benito', 'Mussolini'),
    ('Hideki', 'Tojo')
]

ww2_leaders.sort()
print(ww2_leaders)

# Control order with lambda function:
ww2_leaders.sort(key=lambda leader: (leader[1], leader[0]))
print('Leaders sorted by last name, first name', ww2_leaders, '-'*70, sep='\n')

# Fix "de Gaulle" sequence issue:
ww2_leaders.sort(key=lambda leader: (leader[1].lower(), leader[0]))
print('Leaders sorted by last name, first name with \"de Gaulle\" fix', ww2_leaders, '-'*70, sep='\n')