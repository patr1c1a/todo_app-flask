from flaskr.task import Task


class TaskManager:
	def __init__(self):
		self.storage = []

	# storing in a list for now. TODO: change storage to database
	def add_new_task(self, task_name, task_status):
		task = Task(task_name, task_status)
		self.storage.append(task)
		return self.storage
