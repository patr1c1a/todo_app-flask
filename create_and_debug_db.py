import sqlite3
from contextlib import closing

db_name = "flaskr/todo_app.db"


def create_db():
    """
    Use this to create a new database for the first time and create the needed table(s).
    """
    sql = """CREATE TABLE tasks
    (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL);"""
    with closing(sqlite3.connect(db_name)) as con, con, closing(con.cursor()) as cur:
        cur.execute(sql)


def populate_test_data():
    """
    Use this to insert test data in the database
    """
    records = [("test task pending", "pending"), ("test task done", "done")]
    sql = "INSERT INTO tasks (name,status) VALUES (?,?)"
    with closing(sqlite3.connect(db_name)) as con, con, closing(con.cursor()) as cur:
        cur.executemany(sql, records)


def view_table(table):
    """
    Use this to print the contents of a table, for debugging purposes.
    :param table: str
    """
    sql = "SELECT * FROM " + table
    with closing(sqlite3.connect(db_name)) as con, con, closing(con.cursor()) as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)


# Only call create_db() before running the app for the first time
# create_db()
# populate_test_data()
view_table("tasks")
