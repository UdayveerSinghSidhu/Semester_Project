import sqlite3
import datetime

class customer:
    def __init__(self, account_number):
        
        self.account_number = account_number
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()

    def get_balance(self):

        self.cursor.execute("""
        SELECT balance FROM accounts
        WHERE account_number = ?
        """, (self.account_number,))

        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            return None
        
    
    def deposit(self, amount):

        balance = self.get_balance()

        if balance is None:
            print("Account not found")
            return

        if amount <= 0:
            print("Amount should be greater than 0")
            return

        if amount < 50:
            print("Deposit amount should be atleast Rs. 50")
            return

        self.cursor.execute("""
        UPDATE accounts
        SET balance = balance + ?
        WHERE account_number = ?
        """, (amount, self.account_number))

        self.conn.commit()

        self.record_transaction("Deposit", amount)

        print(f"{amount} Rs. credited successfully")

    
    def withdraw(self, amount):

        balance = self.get_balance()

        if balance is None:
           print("Account not found")
           return

        if amount <= 0:
           print("Amount should be greater than 0")
           return

        if amount > balance:
           print("Insufficient Balance")
           return

        self.cursor.execute("""
        UPDATE accounts
        SET balance = balance - ?
        WHERE account_number = ?
        """, (amount, self.account_number))

        self.conn.commit()

        self.record_transaction("Withdraw", amount)

        print(f"{amount} Rs. debited successfully")


    def record_transaction(self, t_type, amount):

        date = datetime.datetime.now()

        self.cursor.execute("""
        INSERT INTO transactions(account_number, type, amount, date)
        VALUES (?, ?, ?, ?)
        """, (self.account_number, t_type, amount, date))

        self.conn.commit()

    def display(self):
        
        self.cursor.execute("""
        SELECT name, account_number, balance
        FROM accounts
        WHERE account_number = ?
        """, (self.account_number,))

        result = self.cursor.fetchone()

        if result:

            print("\nCustomer Details:")
            print("Name:", result[0])
            print("Account Number:", result[1])
            print("Balance: Rs.", result[2])

        else:
            print("Account not found")
    
    def close_connection(self):

        self.conn.close()



