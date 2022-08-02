import enum


class TaskStatus(enum.Enum):
	PENDING = 1
	DONE = 2


class Task:
	def __init__(self, task_id: int, name: str, status: TaskStatus) -> None:
		self.id = task_id
		self.name = name
		self.status = status

	def serialize(self) -> dict:
		"""
		Converts class attributes to a dict so it can be easily serialized into JSON.
		:return: dict
		"""
		return {"task_id": self.id,
			"task_name": self.name,
			"task_status": self.status}
