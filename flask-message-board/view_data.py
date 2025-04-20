import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('SELECT * FROM messages')
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
