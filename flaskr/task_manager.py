from typing import List
from flaskr.task import Task, TaskStatus


class TaskManager:
    def __init__(self) -> None:
        self.storage = []

    def create_task(self, name: str, status: str) -> Task:
        """
        Creates a new Task with the given parameters.
        :param name: str
        :param status: TaskStatus
        :return: Task
        """
        next_id = len(self.storage) + 1
        enum_status = TaskStatus[status.upper()]
        return Task(task_id=next_id, name=name, status=enum_status)

    def add_task(self, task: Task) -> List:
        """
        Stores the task. The storage uses a list for now.
        TODO: change storage to database. next_id will be replaced with a database generated id.
        :param task: Task
        :return: List
        """
        self.storage.append(task)
        return self.storage

    def delete_task(self, task_id: int) -> bool:
        """
        Given a task id, it removes a task from storage if its id matches the parameter.
        Returns True if deletion was successful (i.e.: the item was found and deleted), False otherwise.
        :param task_id: int
        :return: bool
        """
        deleted = False
        for task in self.storage:
            if task.id == task_id:
                self.storage.remove(task)
                deleted = True
        return deleted

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
