import mysql.connector
import csv

connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

query = """SELECT year(debut) AS year, avg(weight) AS weight
FROM people
WHERE debut is NOT NULL
GROUP BY year(debut)
ORDER BY year(debut)"""

cursor = connection.cursor(dictionary=True)
cursor.execute(query)
results = cursor.fetchall()

cursor.close()
connection.close()

csv_file = '../data/mlb-weight-over-time.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = results[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)