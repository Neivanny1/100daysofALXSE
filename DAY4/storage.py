import json

#path to json file used as storage
tasks_file = "tasks.json"

'''
Function to reads tickets submitted by complaints
'''
def read_tasks():
  try:
    with open(tasks_file, 'r') as file:
      tasks = json.load(file)
  except FileNotFoundError:
    tasks = {}
  return tasks

'''
Function to write activities to JSON file
'''
def write_tasks(tasks):
  with open(tasks_file, 'w') as file:
    json.dump(tasks, file, indent=4)
