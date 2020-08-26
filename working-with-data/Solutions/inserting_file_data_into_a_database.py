import sqlite3
connection = sqlite3.connect(':memory:')
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

create = """CREATE TABLE states (
                'state' text,
                'pop2020' integer,
                'pop2000' integer
            )"""

cursor.execute(create)

insert = 'INSERT INTO states VALUES (?, ?, ?)'

data = []
with open('../data/states.txt') as f:
    for line in f.readlines():
        state_data = line.split('\t')
        tpl_state_data = (state_data[0],
                          int(state_data[1].replace(',','')),
                          int(state_data[2].replace(',','')))
                          
        data.append(tpl_state_data)

cursor.executemany(insert, data)

select = """SELECT state,
            CAST((pop2020*1.0/pop2000) * pop2020 AS INTEGER) AS pop2040
            FROM states ORDER BY pop2040 DESC"""

cursor.execute(select)

results = cursor.fetchall()
cursor.close()
connection.close()

for record in results:
    state = record['state']
    pop2040 = record['pop2040']
    print(f'The projected 2040 population of {state} is {pop2040:,}.')