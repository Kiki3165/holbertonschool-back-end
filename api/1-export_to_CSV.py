#!/usr/bin/python3
"""docu"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Get employee ID from command line arguments
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)
    employee_id = int(sys.argv[1])

    # Fetch employee name
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    user = user_response.json()
    employee_name = user.get("name")

    # Fetch tasks for the employee
    tasks_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
    tasks = tasks_response.json()

    # Export tasks to CSV
    with open('{}.csv'.format(employee_id), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in tasks:
            writer.writerow([task.get('userId'), employee_name, task.get('completed'), task.get('title')])
