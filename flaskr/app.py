from flask import Flask, request, jsonify
from flaskr.task_manager import TaskManager

app = Flask(__name__)


@app.route('/add/')
def add():
    task = request.args.get("task_name")
    result = TaskManager.add_new_task(task)
    return jsonify(result)


if __name__ == '__main__':
    manager = TaskManager()
    app.run(debug=True)
