import psycopg2

def create():
    db_connection = psycopg2.connect("dbname='local_db_1' user='postgres' password='password' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # REAL is a float
    db_connection.commit()
    db_connection.close()

def insert(item, quantity, price):
    db_connection = psycopg2.connect("dbname='local_db_1' user='postgres' password='password' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    db_connection.commit()
    db_connection.close()

def view():
    db_connection = psycopg2.connect("dbname='local_db_1' user='postgres' password='password' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM store")
    rows = db_cursor.fetchall()
    db_connection.close()
    return rows

def delete(item):
    db_connection = psycopg2.connect("dbname='local_db_1' user='postgres' password='password' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    db_connection.commit()
    db_connection.close()

def update(item, quantity, price):
    db_connection = psycopg2.connect("dbname='local_db_1' user='postgres' password='password' host='localhost'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("UPDATE store SET price=%s, quantity=%s WHERE item=%s", (price, quantity, item))
    db_connection.commit()
    db_connection.close()

# create()
# insert("Macbook", 1, 100000)
# insert("Tablet", 2, 140999)
# insert("Toshiba", 10, 30000)
# insert("Infinix", 3, 12000)
# print(view())
# delete("Toshiba")
# update("Macbook", 14, 199990.9)
print(view())
