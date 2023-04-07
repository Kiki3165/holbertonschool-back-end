#!/usr/bin/python3
"""docu"""

import requests
import sys

url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos"

response = requests.get(url)

if response.status_code != 200:
    print("Error: Could not retrieve TODO list data for employee ID", sys.argv[1])
    sys.exit(1)

todos = response.json()

total_tasks = len(todos)
completed_tasks = sum(todo["completed"] for todo in todos)

print(f"Employee {todos[0]['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

for todo in todos:
    if todo["completed"]:
        print(f"\t{todo['title']}")
