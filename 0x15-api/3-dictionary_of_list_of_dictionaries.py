#!/usr/bin/python3
""" using a REST API, Records all tasks from all employees in a json
"""
import json
import requests

if __name__ == "__main__":
    """ script
    """
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get('{}users/'.format(url)).json()
    tasks = requests.get('{}todos'.format(url)).json()

    json_str = {}
    for usr in users:
        id = usr.get('id')
        tasks_list = []
        for elem in tasks:
            if id == elem.get('userId'):
                data = {
                    'task': elem.get('title'),
                    'completed': elem.get('completed'),
                    'username': usr.get('username')
                }
                tasks_list.append(data)
        json_str.update({str(id): tasks_list})
    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as f:
        json.dump(json_str, f)
