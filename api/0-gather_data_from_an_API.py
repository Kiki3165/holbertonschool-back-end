#!/usr/bin/python3
"""docu"""

import urllib.request
import json
import sys

if __name__ == '__main__':
    """docu"""
    employee_id = int(sys.argv[1])
    url_id = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    api_response_employee = requests.get(url_id)
    employee_json = api_response_employee.json()
    EMPLOYEE_NAME = employee_json.get('name')

    """docu"""
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    api_response_todos = requests.get(url_todo)
    user_tasks_json = api_response_todos.json()
    employee_todo = None
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for todo in user_tasks_json:
        if todo.get("userId") == int(employee_id):
            employee_todo = todo
            if employee_todo.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done "
          f"with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in TASK_TITLE:
        print(f"\t {task}")