#!/usr/bin/python3
""" using a REST API, for a given employee ID, returns information
    about his/her TO-DO list progress in a CSV
"""
import requests
import sys
import csv

if __name__ == "__main__":
    """ script
    """
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get('{}users/{}'.format(url, id)).json()

    id_param = {'userId': id}
    tasks = requests.get('{}todos'.format(url), params=id_param).json()

    csv_file = "{}.csv".format(id)
    with open(csv_file, mode='w') as user_file:
        user_writer = csv.writer(user_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for elem in tasks:
            user_writer.writerow((id, user_data.get(
                'username'), elem.get('completed'), elem.get('title')))
