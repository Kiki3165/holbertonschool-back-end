#!/usr/bin/python3
"""docu"""

import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    USER_ID = sys.argv[1]
    url_id = f'{url}/users/{USER_ID}'
    api_response_employee = requests.get(url_id)
    employee_json = api_response_employee.json()
    USERNAME = employee_json.get('username')

    url_tasks = f'{url}/todos?userId={USER_ID}'
    api_response_tasks = requests.get(url_tasks)
    task_json = api_response_tasks.json()

    tasks = []
    for task in task_json:
        tasks.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': USERNAME
        })
    
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(todo_all_employees, json_file)
