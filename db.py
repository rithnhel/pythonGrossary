import sqlite3
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS keyword(
            id Integer Primary Key, titleName text, description text, example text)
            """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, titleName, description, example):
        self.cur.execute("INSERT INTO keyword VALUES (NULL,?,?,?)",
                         (titleName, description, example))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * FROM keyword")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE FROM keyword WHERE id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, titleName, description, example):
        self.cur.execute("""
        UPDATE keyword SET titleName=?, description=?, example=? WHERE id=?
        """,
                         (titleName, description, example, id))
        self.con.commit()
