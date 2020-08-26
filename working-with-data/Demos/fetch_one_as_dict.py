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

cursor = connection.cursor(dictionary=True)
cursor.execute(query)
result = cursor.fetchone()

if result:
    player_name = result['nameFirst'] + ' ' + result['nameLast']
    birth_place = result['birthCity'] + ', ' + result['birthState']
    birth_year = result['birthYear']
    print(f'{player_name} was born in {birth_place} in {birth_year}.')
else:
    print('No records returned.')

cursor.close()
connection.close()