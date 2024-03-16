import json


'''
Function to reads task closed by techs
'''
def read_storage(db):
  try:
    with open(db, 'r') as file:
      tasks = json.load(file)
  except FileNotFoundError:
    tasks = {}
  return tasks

'''
Function to write activities to JSON file
'''
def write_storage(db,tasks):
  with open(db, 'w') as file:
    json.dump(tasks, file, indent=4)
