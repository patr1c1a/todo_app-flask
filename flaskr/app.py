from flask import Flask, request, jsonify, Response
from flaskr.task_manager import TaskManager
from flaskr.task import TaskStatus

app = Flask(__name__)


@app.route("/add/")
def add() -> Response:
    """
    Endpoint (supported verbs: GET).
    Gets parameters from the request to create a new Task object, then adds it to storage.
    :return: Response (JSON)
    """


@app.route("/add/", methods=["POST"])
def add() -> Response:
    """
    Endpoint (supported verbs: POST).
    Gets parameters from the request to create a new Task object, then adds it to storage.
    :return: Response (JSON)
    """
    task_name = request.args.get("task_name")
    task_status = request.args.get("task_status")
    task = manager.create_task(name=task_name, status=task_status)
    tasks = manager.add_task(task=task)
    return jsonify([task.serialize() for task in tasks])


@app.route("/delete/", methods=["POST"])
def delete() -> Response:
    """
    Endpoint (supported verbs: POST).
    Gets a task id as a parameter from the request and then removes the matching task from storage.
    Returns true if the task was found and deleted, false otherwise.
    :return: Response (JSON)
    """
    task_id = int(request.args.get("task_id"))
    result = manager.delete_task(task_id=task_id)
    return jsonify(result)


@app.route("/list_tasks/")
def list_tasks() -> Response:
    """
    Endpoint (supported verbs: GET).
    Gets a list of tasks in storage. If the request has no parameters, it lists all tasks.
    If the request has a 'task_status' parameter (which can either be 'done' or 'pending'), it returns a filtered list.
    :return: Response (JSON)
    """
    task_status = request.args.get("task_status")
    if task_status:
        filtered = manager.filter_tasks(task_status)
        return jsonify([task.serialize() for task in filtered])
    return jsonify([task.serialize() for task in manager.storage])


@app.route("/mark/", methods=["GET", "POST"])
def mark() -> Response:
    """
    Endpoint (supported verbs: GET, POST).
    Gets a task id as a parameter from the request and then changes the matching task's status.
    Returns true if the task was found and marked, false otherwise.
    :return: Response (JSON)
    """
    task_id = int(request.args.get("task_id"))
    task_status = request.args.get("task_status")
    result = manager.mark_task(task_id=task_id, status=task_status)
    return jsonify(result)
    task = manager.create_task(name=task_name, status=task_status)
    tasks = manager.add_task(task=task)
    return jsonify([task.serialize() for task in tasks])


@app.route("/delete/", methods=["DELETE"])
def delete() -> Response:
    """
    Endpoint (supported verbs: DELETE).
    Gets a task id as a parameter from the request and then removes the matching task from storage.
    Returns true if the task was found and deleted, false otherwise.
    :return: Response (JSON)
    """
    task_id = int(request.args.get("task_id"))
    result = manager.delete_task(task_id=task_id)
    return jsonify(result)


@app.route("/list_tasks/")
def list_tasks() -> Response:
    """
    Endpoint (supported verbs: GET).
    Gets a list of tasks in storage. If the request has no parameters, it lists all tasks.
    If the request has a 'task_status' parameter (which can either be 'done' or 'pending'), it returns a filtered list.
    :return: Response (JSON)
    """
    status = request.args.get("task_status")
    if status:
        filtered = manager.filter_tasks(TaskStatus[status.upper()])
        return jsonify([task.serialize() for task in filtered])
    return jsonify([task.serialize() for task in manager.storage])


if __name__ == "__main__":
    manager = TaskManager()
    app.run(debug=True)
