#!/usr/bin/python3
"""docu"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    user_request = requests.get(user_url)
    tasks_request = requests.get(tasks_url)

    employee_name = user_request.json().get('name')
    tasks = tasks_request.json()

    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get('completed')]

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))

    with open('{}.csv'.format(employee_id), mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id,
                             employee_name,
                             task.get('completed'),
                             task.get('title')])
