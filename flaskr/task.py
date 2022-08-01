class Task:
	def __init__(self, name, status):
		self.name = name
		self.status = status

	def serialize(self):
		return {"task_name": self.name,
				"task_status": self.status}
