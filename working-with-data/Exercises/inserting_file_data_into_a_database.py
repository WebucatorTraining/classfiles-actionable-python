import sqlite3
connection = sqlite3.connect(':memory:')
connection.row_factory = sqlite3.Row

# Create the cursor.

create = """CREATE TABLE states (
                'state' text,
                'pop2020' integer,
                'pop2000' integer
            )"""

# Execute the create statement.

insert = 'INSERT INTO states VALUES (?, ?, ?)'

# Create a list of tuples from the data in '../data/states.txt'.

# Insert the data into the database.

select = """SELECT state,
            CAST((pop2020*1.0/pop2000) * pop2020 AS INTEGER) AS pop2040
            FROM states ORDER BY pop2040 DESC"""

# Execute the select statement.

# Fetch the rows into a variable.

# Close the cursor and connection.

results = cursor.fetchall()
cursor.close()
connection.close()

# Print out the results.