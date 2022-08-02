from flaskr.task import Task


class TaskManager:
	def __init__(self) -> None:
		self.storage = []

	def add_new_task(self, task_name, task_status) -> list:
		"""
		Creates a new Task with the given parameters and then stores it. The storage uses a list for now.
		TODO: change storage to database. next_id will be replaced with a database generated id.
		:param task_name: str
		:param task_status:
		:return:
		"""
		next_id = len(self.storage)+1
		task = Task(next_id, task_name, task_status)
		self.storage.append(task)
		return self.storage
