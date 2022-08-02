from flaskr.task import Task


class TaskManager:
	def __init__(self):
		self.storage = []

	# storing in a list for now. TODO: change storage to database
	def add_new_task(self, task_name, task_status):
		next_id = len(self.storage)+1  # will be replaced with database generated id
		task = Task(next_id, task_name, task_status)
		self.storage.append(task)
		return self.storage
