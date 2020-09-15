#!/usr/bin/python3
#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
    about his/her TO-DO list progress in a json
"""
import requests
import sys
import json

if __name__ == "__main__":
    """ script
    """
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get('{}users/{}'.format(url, id)).json()

    id_param = {'userId': id}
    tasks = requests.get('{}todos'.format(url), params=id_param).json()
    tasks_list = []
    for elem in tasks:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': user_data.get('username')
        }
        tasks_list.append(data)
    json_str = {str(id): tasks_list}

    json_file = "{}.json".format(id)
    with open(json_file, 'w') as f:
        json.dump(json_str, f)
