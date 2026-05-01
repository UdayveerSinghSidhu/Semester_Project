import sqlite3

def check_login(username):

    username = username.strip()

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT password_hash
    FROM users
    WHERE TRIM(LOWER(username)) = TRIM(LOWER(?))
    """, (username,))

    result = cursor.fetchone()

    conn.close()

    return result
