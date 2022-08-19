from flask import Flask, request, jsonify, Response
from flaskr.task_manager import TaskManager

app = Flask(__name__)


@app.route("/add/", methods=["POST"])
def add() -> Response:
    """
    Endpoint.
    Gets parameters from the request to create a new Task object, then adds it to storage.
    :return: Response (JSON)
    """
    task_name = request.args.get("task_name")
    task_status = request.args.get("task_status")
    result = manager.add_task(name=task_name, status=task_status)
    return jsonify(result)


@app.route("/delete/", methods=["DELETE"])
def delete() -> Response:
    """
    Endpoint.
    Gets a task id as a parameter from the request and then removes the matching task from storage.
    Returns true if the task was found and deleted, false otherwise.
    :return: Response (JSON)
    """
    task_id = int(request.args.get("task_id"))
    result = manager.delete_task(task_id=task_id)
    return jsonify(result)


@app.route("/list_tasks/", methods=["GET"])
def list_tasks() -> Response:
    """
    Endpoint.
    Lists tasks. If the request has no parameters, it lists all tasks.
    If the request has a 'task_status' parameter (which can either be 'done' or 'pending'), it returns a filtered list.
    :return: Response (JSON)
    """
    task_status = request.args.get("task_status")
    result = manager.list_tasks(status=task_status)
    return jsonify(result)


@app.route("/change_status/", methods=["PUT"])
def change_status() -> Response:
    """
    Endpoint.
    Gets a task id as a parameter and updates the task status for the matching row in the database.
    If the new status is the same as the old status, the update is still executed but no change will be perceived.
    Returns true if the task was found in the database, false otherwise.
    :return: Response (JSON)
    """
    task_id = int(request.args.get("task_id"))
    new_status = request.args.get("task_status")
    result = manager.change_status(task_id=task_id, status=new_status)
    return jsonify(result)


if __name__ == "__main__":
    manager = TaskManager()
    app.run(debug=True)
