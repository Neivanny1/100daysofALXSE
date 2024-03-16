from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Sample JSON file to store activities
activities_file = "activities.json"

# Function to read activities from JSON file
def read_activities():
    try:
        with open(activities_file, 'r') as file:
            activities = json.load(file)
    except FileNotFoundError:
        activities = {}
    return activities

# Function to write activities to JSON file
def write_activities(activities):
    with open(activities_file, 'w') as file:
        json.dump(activities, file, indent=4)

# Endpoint to add new activity
@app.route('/activities', methods=['POST'])
def add_activity():
    data = request.json
    title = data.get('title')
    body = data.get('body')
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if title and body:
        activities = read_activities()
        activity_id = len(activities) + 1
        activities[activity_id] = {
            "title": title,
            "body": body,
            "time_created": time_created
        }
        write_activities(activities)
        return jsonify({"message": f"Activity with ID {activity_id} added successfully"}), 201
    else:
        return jsonify({"message": "Title and body are required fields"}), 400

# Endpoint to get all activities
@app.route('/activities', methods=['GET'])
def get_all_activities():
    activities = read_activities()
    return jsonify(activities)

# Endpoint to get activity by ID
@app.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    activities = read_activities()
    activity = activities.get(activity_id)
    if activity:
        return jsonify(activity)
    else:
        return jsonify({"message": "Activity not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
