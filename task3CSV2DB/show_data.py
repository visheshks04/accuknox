import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
users= cursor.fetchall()

for user in users:
    print(f"user: {user}")

conn.close()
