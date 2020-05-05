#!/usr/bin/python3
""" Python script to export data in the JSON format """

import json
import requests
import sys


if __name__ == "__main__":
    """ Records all tasks from all employees """

    urlUser = "https://jsonplaceholder.typicode.com/users/"
    urlTODO = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(urlUser, verify=False).json()
    TODO = requests.get(urlTODO, verify=False).json()

    dirUsers = {}
    dirUsername = {}

    for i in user:
        ID = i.get('id')
        dirUsers[ID] = []
        dirUsername[ID] = i.get('username')

    for task in TODO:
        dir_tasks = {}
        ID = task.get('userId')
        dir_tasks['task'] = task.get('title')
        dir_tasks['completed'] = task.get('completed')
        dir_tasks['username'] = dirUsername.get(ID)
        dirUsers.get(ID).append(dir_tasks)

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(dirUsers, f)
