import sqlite3

class Backend(object):

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, client TEXT, product TEXT, sp REAL, profit REAL)")
        self.conn.commit()
       
    def insert(self, client, product, sp, profit):
        self.cur.execute("INSERT INTO sales VALUES (NULL,?,?,?,?)",(client, product, sp, profit))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM sales")
        rows = self.cur.fetchall()
        return rows

    def search(self, client="", product="", sp="", profit=""):
        self.cur.execute("SELECT * FROM sales WHERE client=? OR product=? OR sp=? OR profit=?", (client, product, sp, profit))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM sales WHERE id=?",(id,))
        self.conn.commit()
       
    def update(self, id, client, product, sp, profit):
        self.cur.execute("UPDATE sales SET client=?, product=?, sp=?, profit=? WHERE id=?",(client, product, sp, profit, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
