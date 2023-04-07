#!/usr/bin/python3
"""docu"""
import csv
import requests
import sys

employee_id = int(sys.argv[1])

"""Get employee name"""
url_employee = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
response_employee = requests.get(url_employee)
employee_json = response_employee.json()
employee_name = employee_json.get('name')

"""Get user tasks"""
url_todo = 'https://jsonplaceholder.typicode.com/todos'
response_todo = requests.get(url_todo)
user_tasks_json = response_todo.json()

"""Filter tasks for the given employee ID"""
employee_tasks = [task for task in user_tasks_json if task.get('userId') == employee_id]

"""Count completed tasks and record task details in CSV format"""
num_completed_tasks = 0
with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for task in employee_tasks:
        if task.get('completed'):
            num_completed_tasks += 1
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

"""Print progress information"""
num_tasks = len(employee_tasks)
print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_tasks}):")
for task in employee_tasks:
    if task.get('completed'):
        print(f"\t {task.get('title')}")
