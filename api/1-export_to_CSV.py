#!/usr/bin/python3
"""docu"""
import csv
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

    with open(f'{USER_ID}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in task_json:
                writer.writerow([USER_ID, USERNAME,
                                 task.get('completed'), task.get('title')])