#!/usr/bin/python3
"""docu"""

import requests
import sys

# API endpoint and employee ID
url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"

# Make API request
response = requests.get(url)

# Check if API request was successful
if response.status_code != 200:
    print("Error: Could not retrieve TODO list data for employee ID", sys.argv[1])
    sys.exit(1)

# Parse JSON response
todos = response.json()

# Calculate TODO list progress
total_tasks = len(todos)
completed_tasks = sum(todo["completed"] for todo in todos)

# Display TODO list progress
print(f"Employee {todos[0]['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

# Display completed tasks
for todo in todos:
    if todo["completed"]:
        print(f"\t{todo['title']}")
