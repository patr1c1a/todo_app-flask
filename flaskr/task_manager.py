class TaskManager:
	def __init__(self):
		self.storage = []

	def add_new_task(self, task):
		self.storage.append(task)
		return self.storage
