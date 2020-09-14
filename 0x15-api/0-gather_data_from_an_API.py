#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
    about his/her TO-DO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    """ script
    """
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get('{}users/{}'.format(url, id)).json()

    id_param = {'userId': id}
    tasks = requests.get('{}todos'.format(url), params=id_param).json()

    tasks_done = [elem for elem in tasks if elem.get("completed") is True]

    print('Employee {} is done with tasks({}/{}):'.format(
        user_data.get('name'), len(tasks_done), len(tasks)))

    for elem in tasks_done:
        print('\t {}'.format(elem.get('title')))
