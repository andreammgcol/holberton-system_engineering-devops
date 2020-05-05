#!/usr/bin/python3
""" Python script to export data in the JSON format """

import json
import requests
import sys


if __name__ == "__main__":
    """ This export data in the JSON format """

    ID = int(sys.argv[1])
    urlUser = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    urlTODO = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)
    user = requests.get(urlUser).json()
    TODO = requests.get(urlTODO).json()

    list_tasks = []

    for task in TODO:
        dir_tasks = {}
        dir_tasks['task'] = task.get('title')
        dir_tasks['completed'] = task.get('completed')
        dir_tasks['username'] = user.get('username')
        list_tasks.append(dir_tasks)

    dir_json = {}
    dir_json[ID] = list_tasks

    with open("{}.json".format(ID), mode='w') as f:
        json.dump(dir_json, f)
