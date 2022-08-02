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
    result = manager.add_new_task(task_name, task_status)
    return jsonify([e.serialize() for e in result])


if __name__ == '__main__':
    manager = TaskManager()
    app.run(debug=True)
