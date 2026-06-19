import sqlite3

conn = sqlite3.connect("finance.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM entries")
rows = cursor.fetchall()

print("Rows:")
for row in rows:
    print(row)

conn.close()