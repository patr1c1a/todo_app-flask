from typing import List
from flaskr.db_manager import DbManager
from task import TaskStatus


class TaskManager:
    """
    Performs any additional data processesing.
    """

    def __init__(self) -> None:
        self.storage = DbManager()

    def add_task(self, name: str, status: str) -> int:
        """
        Sends the parameters to the storage handler which inserts them into the DB as a new task. Returns the id of the
        newly created task.
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

    def list_tasks(self, status: str) -> List:
        """
        Lists tasks with the specified status (all tasks if no status is given).
        :param status: str
        :return: List
        """
        enum_status = None
        if status:
            enum_status = TaskStatus[status.upper()]
        return self.storage.list_tasks(status_filter=enum_status)

    def change_status(self, task_id: int, status: str) -> bool:
        """
        Given a task id, it updates the task status if it's found in the database.
        Returns True if update was successful (i.e.: the item was found and updated), False otherwise.
        :param task_id: int
        :param status: str
        :return: bool
        """
        enum_status = TaskStatus[status.upper()]
        result = self.storage.update_task(task_id=task_id, status=enum_status)
        return result == 1
