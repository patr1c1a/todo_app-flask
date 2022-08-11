from typing import List
import sqlite3
from contextlib import closing


class DbManager:
    def __init__(self) -> None:
        self.db_name = "todo_app.db"

    def insert_task(self, task_name: str, task_status: str) -> int:
        """
        Inserts a new task in the database. Returns the autogenerated task id.
        :param task_name: str
        :param task_status: str
        :return: int
        """
        params = [task_name, task_status]
        sql = "INSERT INTO tasks (name,status) VALUES (?,?)"
        with closing(sqlite3.connect(self.db_name)) as con, con, closing(
            con.cursor()
        ) as cur:
            cur.execute(sql, params)
            return cur.lastrowid

    def delete_task(self, task_id: int) -> int:
        """
        Deletes from the database the task matching the given id. Returns number of rows deleted (1 if task was found,
        0 if it wasn't).
        :param task_id: int
        :return: int
        """
        params = [task_id]
        sql = "DELETE FROM tasks WHERE task_id = ?"
        with closing(sqlite3.connect(self.db_name)) as con, con, closing(
            con.cursor()
        ) as cur:
            cur.execute(sql, params)
            return cur.rowcount

    def list_tasks(self, status_filter: str) -> List:
        """
        Gets tasks from the database. If there's a status_filter, it returns only tasks matching it. If status_filter
        is None, it returns all rows in the table.
        :param status_filter: str
        :return: List
        """
        params = []
        sql = "SELECT * FROM tasks"
        with closing(sqlite3.connect(self.db_name)) as con, con, closing(
            con.cursor()
        ) as cur:
            if status_filter:
                params.append(status_filter)
                sql += " WHERE status = ?"
            cur.execute(sql, params)
            return cur.fetchall()

    def update_task(self, task_id: int, status: str) -> int:
        """
        Updates the task matching the given id in the database. Returns number of rows affected (1 if task was found,
        0 if it wasn't).
        :param task_id: int
        :param status: str
        :return: int
        """
        params = [status, task_id]
        sql = "UPDATE tasks SET status = ? WHERE task_id = ?"
        with closing(sqlite3.connect(self.db_name)) as con, con, closing(
            con.cursor()
        ) as cur:
            cur.execute(sql, params)
            return cur.rowcount
