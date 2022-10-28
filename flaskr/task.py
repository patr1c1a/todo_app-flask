from typing import Dict
from enum import Enum


class TaskStatus(Enum):
    PENDING = "PENDING"
    DONE = "DONE"


class Task:
    def __init__(self, task_id: int, name: str, status: TaskStatus) -> None:
        self.id = task_id
        self.name = name
        self.status = status

    def serialize(self) -> Dict:
        """
        Converts class attributes to a dict so it can be easily serialized into JSON.
        :return: Dict
        """
        return {"task_id": self.id, "task_name": self.name, "task_status": self.status}
