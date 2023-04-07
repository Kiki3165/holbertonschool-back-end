#!/usr/bin/python3
# docu

import requests
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    # Get a list of all users
    users_response = requests.get(f'{url}/users')
    users_json = users_response.json()

    # Create an empty dictionary to store tasks for all users
    all_tasks = {}

    for user in users_json:
        user_id = user['id']
        username = user['username']

        # Get tasks for the current user
        tasks_response = requests.get(f'{url}/todos?userId={user_id}')
        tasks_json = tasks_response.json()

        # Create a list to store tasks for the current user
        user_tasks = []

        for task in tasks_json:
            task_title = task['title']
            task_completed = task['completed']
            user_task = {
                'username': username,
                'task': task_title,
                'completed': task_completed
            }
            user_tasks.append(user_task)

        # Add the list of tasks for the current user to the dictionary
        all_tasks[user_id] = user_tasks

        # Write tasks for the current user to a JSON file
        with open(f'{user_id}.json', 'w') as f:
            json.dump(user_tasks, f)

    # Write tasks for all users to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
