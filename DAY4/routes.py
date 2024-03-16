from flask import Flask, jsonify, request
from datetime import datetime
from storage import *
import json


app = Flask(__name__)

@app.route('/')
def home():
  return 'Ticketing system'
'''
Function for adding a new task
'''
@app.route('/tasks', methods=['POST', 'GET'])
def add_task():
  if request.method == 'POST':
    data = request.json
    task_name  = data.get('task_name')
    task_status = data.get('task_status')
    task_feedback = data.get('task_feedback')
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if task_name and task_status and task_feedback:
      tasks = read_tasks()
      task_id = len(tasks) + 1
      tasks[task_id] = {
        "task_name": task_name,
        "task_status": task_status,
        "task_feedback": task_feedback,
        "time_created": time_created
      }
      write_tasks(tasks)
      return jsonify({"Message": {"Status Code": 201, "Event": f"Task with ID {task_id} created","Time" : f"{time_created}"}}), 201
    else:
      return jsonify({"error": "Forbidden: All fields (task_name, task_status, task_feedback) are required."}), 403
  elif request.method == 'GET':
    '''
    Geting all tasks
    '''
    tasks = read_tasks()
    return jsonify(tasks)