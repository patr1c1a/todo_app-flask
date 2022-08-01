from flask import Flask, request, jsonify
from flaskr.task_manager import TaskManager

app = Flask(__name__)


@app.route('/add/')
def add():
    task_name = request.args.get("task_name")
    task_status = request.args.get("task_status")
    result = manager.add_new_task(task_name, task_status)
    return jsonify([e.serialize() for e in result])


if __name__ == '__main__':
    manager = TaskManager()
    app.run(debug=True)
