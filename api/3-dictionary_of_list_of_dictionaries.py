#!/usr/bin/python3
# docu

import requests
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    users_response = requests.get(f'{url}/users')
    users_json = users_response.json()
    all_tasks = {}
    """docu"""
    for user in users_json:
        user_id = user['id']
        username = user['username']

        tasks_response = requests.get(f'{url}/todos?userId={user_id}')
        tasks_json = tasks_response.json()

        user_tasks = []
        """docu"""
        for task in tasks_json:
            task_title = task['title']
            task_completed = task['completed']
            user_task = {
                'username': username,
                'task': task_title,
                'completed': task_completed
            }
            user_tasks.append(user_task)
        """docu"""
        all_tasks[user_id] = user_tasks
        with open(f'{user_id}.json', 'w') as f:
            json.dump(user_tasks, f)
        with open('todo_all_employees.json', 'w') as f:
            json.dump(all_tasks, f)
