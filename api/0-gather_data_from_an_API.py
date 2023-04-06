#!/usr/bin/python3
"""
Script that retrieves information about an employee's TODO list progress
"""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

    r = requests.get(url)
    todos = r.json()

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    employee_name = user.get('name')

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'.format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print('\t {} {}'.format('\t', task.get('title')))
