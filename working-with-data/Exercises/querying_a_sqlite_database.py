import sqlite3
connection = sqlite3.connect('../data/lahmansbaseballdb.sqlite')
connection.row_factory = sqlite3.Row

query = """SELECT nameFirst, nameLast, weight, 
                  debut AS debut
           FROM people
           ORDER BY weight DESC
           LIMIT 5"""

# YOUR CODE HERE