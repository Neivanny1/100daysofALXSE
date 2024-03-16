from flask import Flask, jsonify, request
from datetime import datetime
from storage import *
import json


app = Flask(__name__)
# file to store and read
task_file = 'tasks.json'
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
    problem = data.get('problem')
    task_status = data.get('task_status')
    task_feedback = data.get('task_feedback')
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if task_name and task_status and task_feedback:
      tasks = read_storage(task_file)
      task_id = len(tasks) + 1
      tasks[task_id] = {
        "task_name": task_name,
        "task_status": task_status,
        "problem": problem,
        "task_feedback": task_feedback,
        "time_created": time_created
      }
      write_storage(task_file, tasks)
      return jsonify({"Message": {"Status Code": 201, "Event": f"Task with ID {task_id} created","Time" : f"{time_created}"}}), 201
    else:
      return jsonify({"Error": "Forbidden: All fields (task_name, task_status, task_feedback) are required."}), 403
  elif request.method == 'GET':
    '''
    Geting all tasks
    '''
    tasks = read_storage(task_file)
    return jsonify(tasks)

'''
Getting each task individually with its ID
'''
@app.route('/task/<int:task_id>')
def get_task_by_id(task_id):
  tasks = read_storage(task_file)
  task = tasks.get(str(task_id))
  if task:
    return jsonify(task)
  else:
    return jsonify({'Error':{"Status": 400, "Message":"Task not found"}})

# file to store and read
issue_file = 'issues.json'
'''
Function for adding a new issue
'''
@app.route('/issues', methods=['POST', 'GET'])
def add_issue():
  if request.method == 'POST':
    data = request.json
    issue_name  = data.get('issue_name')
    issue = data.get('issue')
    issue_status = data.get('issue_status')
    issue_nature = data.get('issue_nature')
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if issue_name and issue_status and issue_nature:
      issues = read_storage(issue_file)
      task_id = len(issues) + 1
      issues[task_id] = {
        "issue_name": issue_name,
        "issue_status": issue_status,
        "issue": issue,
        "issue_nature": issue_nature,
        "time_created": time_created
      }
      write_storage(issue_file, issues)
      return jsonify({"Message": {"Status Code": 201, "Event": f"Issue with ID {task_id} created","Time" : f"{time_created}"}}), 201
    else:
      return jsonify({"Error": "Forbidden: All fields (issue_name, issue_status, issue_nature) are required."}), 403
  elif request.method == 'GET':
    '''
    Geting all issues
    '''
    issues = read_storage(issue_file)
    return jsonify(issues)

'''
Getting each issue individually with its ID
'''
@app.route('/issue/<int:issue_id>')
def get_issue_by_id(issue_id):
  issues = read_storage(issue_file)
  issue = issues.get(str(issue_id))
  if issue:
    return jsonify(issue)
  else:
    return jsonify({'Error':{"Status": 400, "Message":"Issue not found"}})

