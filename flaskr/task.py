class Task:
	def __init__(self, id, name, status):
		self.id = id
		self.name = name
		self.status = status

	def serialize(self):
		return {"task_id": self.id,
			"task_name": self.name,
			"task_status": self.status}
