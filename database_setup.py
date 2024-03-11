from sqlite3 import Connection,connect,Cursor

con:Connection = connect('database.db')
cur:Cursor = Cursor(con)

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