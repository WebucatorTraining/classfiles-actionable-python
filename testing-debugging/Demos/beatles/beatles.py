import sqlite3

class Beatles:
    def __init__(self):
        self._connection = sqlite3.connect(':memory:')
        self._cursor = self._connection.cursor()

    def create(self):
        create = """CREATE TABLE beatles (
            'fname' text,
            'lname' text,
            'nickname' text
        )"""
        self._cursor.execute(create)

    def insert(self):
        members = [
            ('John', 'Lennon', 'The Smart One'),
            ('Paul', 'McCartney', 'The Cute One'),
            ('George', 'Harrison', 'The Funny One'),
            ('Ringo', 'Starr', 'The Quiet One')
        ]

        insert = 'INSERT INTO beatles VALUES (?,?,?)'

        self._cursor.executemany(insert, members)

    def select(self, query):
        self._cursor.execute(query)
        self._cursor.arraysize=2
        return self._cursor.fetchall()

    def select_one(self, query):
        self._cursor.execute(query)
        self._cursor.arraysize=2
        return self._cursor.fetchone()

    def close(self):
        self._cursor.close()