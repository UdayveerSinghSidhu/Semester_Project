import sqlite3
import random

def register_user():

    print("\n=== USER REGISTRATION ===")

    username = input("Enter username: ").strip()

    password = input(
        "Enter password (8 to 12 characters): "
    ).strip()

    if not username or not password:

        print("\n=== INVALID INPUT ===")
        return

    if not (8 <= len(password) <= 12):

        print("\n=== PASSWORD ERROR ===")
        print("Password must be 8–12 characters long")

        return

    try:

        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()

        # Save user
        cursor.execute("""
        INSERT INTO users(username, password_hash)
        VALUES (?, ?)
        """, (username, password))

        # Generate account number
        account_number = random.randint(100000, 999999)

        # Create account automatically
        cursor.execute("""
        INSERT INTO accounts(account_number, name, balance)
        VALUES (?, ?, ?)
        """, (account_number, username, 0))

        conn.commit()

        print("\n=== REGISTRATION SUCCESSFUL ===")
        print("Your Account Number:", account_number)

    except sqlite3.IntegrityError:

        print("\n=== USER EXISTS ===")

    finally:

        conn.close()