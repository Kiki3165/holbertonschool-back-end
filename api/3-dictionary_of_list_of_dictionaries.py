#!/usr/bin/python3
"""docu"""

import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    url_id = f"{url}/users"
    api_response_id = requests.get(url_id)
    id_json = api_response_id.json()

    employees_tasks = {}

    for person in id_json:
        id = person.get('id')
        username = person.get('username')
        url_tasks = f'{url}/todos?userId={id}'
        api_response_tasks = requests.get(url_tasks)
        tasks_json = api_response_tasks.json()
        employee_dict = []
        for task in tasks_json:
            employee_tasks = {"username": username,
                              "task": task.get('title'),
                              "completed": task.get('completed')}
            employee_dict.append(employee_tasks)
        employees_tasks[id] = employee_dict

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employees_tasks, json_file)