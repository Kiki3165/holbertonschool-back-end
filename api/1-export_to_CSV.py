#!/usr/bin/python3
"""docu"""
import requests
import sys
import csv

if __name__ == '__main__':
    """ gets the employee name """
    employee_id = int(sys.argv[1])
    url_id = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    api_response_employee = requests.get(url_id)
    employee_json = api_response_employee.json()
    USERNAME = employee_json.get('username')

    """ gets the list of tasks """
    url_todo = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    api_response_todos = requests.get(url_todo)
    tasks_json = api_response_todos.json()

    """ extracts relevant information and writes to CSV file """
    filename = f'{employee_id}.csv'
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks_json:
            writer.writerow({
                'USER_ID': task.get('userId'),
                'USERNAME': USERNAME,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })
    
    print(f'TODO list for user {USERNAME} has been saved to {filename}')
