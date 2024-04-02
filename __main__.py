from flask import Flask
import TasksDF
import json

app = Flask(__name__)

@app.route("/tasks")
def get_all_tasks():
    all_tasks = TasksDF.get_all_tasks()
    return json.dumps(all_tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    # tasks_db.add_task()
    new_task = {id:5, "title":"new"}
    return json.dumps(new_task)

@app.route("/tasks/<int:task_id>")
def get_single_task(task_id):
    del all_tasks[int(task_id)]
    return json.dumps('deleted')


if __name__ == '__main__':
   app.run(port=5000)