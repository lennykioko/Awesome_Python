import sqlite3

def create():
    db_connection = sqlite3.connect('lite.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # REAL is a float
    db_connection.commit()
    db_connection.close()

def insert(item, quantity, price):
    db_connection = sqlite3.connect('lite.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    db_connection.commit()
    db_connection.close()

def view():
    db_connection = sqlite3.connect('lite.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM store")
    rows = db_cursor.fetchall()
    db_connection.close()
    return rows

def delete(item):
    db_connection = sqlite3.connect('lite.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("DELETE FROM store WHERE item=?", (item,))
    db_connection.commit()
    db_connection.close()

def update(item, quantity, price):
    db_connection = sqlite3.connect('lite.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("UPDATE store SET price=?, quantity=? WHERE item=?", (price, quantity, item))
    db_connection.commit()
    db_connection.close()

# create()
# insert("Macbook", 1, 100000)
# print(view())
# delete('Salary')
# update("Macbook", 2, 120000)
print(view())
