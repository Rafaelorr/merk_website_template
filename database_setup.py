import sqlite3

con:sqlite3.Connection = sqlite3.connect('database.db')
cur:sqlite3.Cursor = sqlite3.Cursor(con)

cur.execute('''CREATE TABLE bestellingen (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            email STRING, 
            postcode INTEGER, 
            straatnaam TEXT, 
            nummer INTEGEER
        )''')
cur.execute('''CREATE TABLE acountcodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        acountcode INTEGER UNQIUE,
        credits INTEGER
)
''')

cur.close()
con.close()