import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
	CREATE IF NOT EXISTS TABLE products (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT
	)
	''')

conn.commit()
conn.close()