import _sqlite3

conn = _sqlite3.connect("bank.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO users(username , password_hash)
VALUES(?, ?)
""", ("admin", "tech@7068"))

conn.commit()

conn.close()

print("user added!")