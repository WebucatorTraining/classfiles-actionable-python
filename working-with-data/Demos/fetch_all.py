# Be sure to install via pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

query = """SELECT nameFirst, nameLast, weight, year(debut)
           FROM people
           ORDER BY weight DESC
           LIMIT 5"""

cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()

cursor.close()
connection.close()

print(results)