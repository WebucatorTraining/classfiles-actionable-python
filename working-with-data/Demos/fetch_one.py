import mysql.connector

connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

query = """SELECT nameFirst, nameLast, birthCity, birthState, birthYear
           FROM people
           WHERE playerID = 'jeterde01';"""

cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchone()

if result:
    player_name = result[0] + ' ' + result[1]
    birth_place = result[2] + ', ' + result[3]
    birth_year = result[4]
    print(f'{player_name} was born in {birth_place} in {birth_year}.')
else:
    print('No records returned.')

cursor.close()
connection.close()