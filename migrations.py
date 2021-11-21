import sqlite3
con = sqlite3.connect('agenda.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, phoneType TEXT, favorite INTEGER)")
cur.execute("INSERT INTO person (name, phone, phoneType, favorite) VALUES ('Joao', '4383749294849', 'Personal', 0)")

con.commit()
con.close()
