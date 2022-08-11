from typing import List
from flaskr.task import Task, TaskStatus
from flaskr.db_manager import DbManager


class TaskManager:
    def __init__(self) -> None:
        self.storage = DbManager()

    def add_task(self, name: str, status: str) -> int:
        """
        Stores the task. The storage uses a list for now.
        TODO: change storage to database. next_id will be replaced with a database generated id.
        :param name: str
        :param status: str
        :return: int
        """
        enum_status = TaskStatus[status.upper()]
        inserted_id = self.storage.insert_task(task_name=name, task_status=enum_status)
        return inserted_id

    def delete_task(self, task_id: int) -> bool:
        """
        Given a task id, it removes the task if found.
        Returns True if deletion was successful (i.e.: the item was found and deleted), False otherwise.
        :param task_id: int
        :return: bool
        """
        result = self.storage.delete_task(task_id=task_id)
        return result == 1

    def filter_tasks(self, status: str) -> List:
        """
        Creates a new list containing the tasks with the specified status.
        :param status: str
        :return: List
        """
        return [
            task for task in self.storage if task.status == TaskStatus[status.upper()]
        ]

    def change_status(self, task_id: int, status: str) -> bool:
        """
        Given a task id, it changes the task status if it's found in storage.
        Returns True if operation was successful (i.e.: the item was found and marked), False otherwise.
        :param task_id: int
        :param status: str
        :return: bool
        """
        marked = False
        for task in self.storage:
            if task.id == task_id:
                task.status = TaskStatus[status.upper()]
                marked = True
        return marked
