from flask import Flask, request, jsonify, Response
from flaskr.task_manager import TaskManager

app = Flask(__name__)


@app.route('/add/')
def add() -> Response:
    """
    Endpoint (supported verbs: GET).
    Gets parameters from the request to create a new Task object, then adds it to storage.
    :return: Response (JSON)
    """
    task_name = request.args.get("task_name")
    task_status = request.args.get("task_status")
    task = manager.create_task(name=task_name, status=task_status)
    tasks = manager.add_task(task=task)
    return jsonify([task.serialize() for task in tasks])


if __name__ == '__main__':
    manager = TaskManager()
    app.run(debug=True)
