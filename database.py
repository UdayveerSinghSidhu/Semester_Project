import _sqlite3

conn = _sqlite3.connect("bank.db")

cursor = conn.cursor()              # conn → connection to the database 
                                    # cursor → a tool to talk to the database for commands

print("Database connected successfully")

conn.close()       # closes the database so resources won't stay busy