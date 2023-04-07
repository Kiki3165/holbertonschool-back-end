#!/usr/bin/python3
"""docu"""

import urllib.request
import json
import sys

# API endpoint and employee ID
url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"

# Make API request
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

# Calculate TODO list progress
total_tasks = len(data)
completed_tasks = sum(todo["completed"] for todo in data)

# Display TODO list progress
print(f"Employee {data[0]['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

# Display completed tasks
for todo in data:
    if todo["completed"]:
        print(f"\t{todo['title']}")
