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
