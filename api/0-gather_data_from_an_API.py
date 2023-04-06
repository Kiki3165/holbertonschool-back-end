#!/usr/bin/python3
"""docu"""

import urllib.request
import json
import sys

import requests
import sys


if __name__ == "__main__":
    # Check if an employee ID was provided as an argument
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve employee ID from command line arguments
    employee_id = sys.argv[1]

    # Retrieve employee information from API
    response_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    response_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))

    # Check if the employee ID is valid
    if response_user.status_code != 200 or response_todos.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    # Parse employee information from response
    employee_info = response_user.json()
    employee_name = employee_info['name']

    # Parse TODO list from response
    todo_list = response_todos.json()
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)

    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task['title']))
