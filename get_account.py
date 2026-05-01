import sqlite3

def get_account_number_by_name(name):

        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT account_number
        FROM accounts
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """, (name,))

        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]
        else:
            return None