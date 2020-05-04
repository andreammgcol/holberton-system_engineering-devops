#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests as req
import json
import sys


if __name__ == "__main__":
    """ That returns information about his/her TODO list progress """
    ID = int(sys.argv[1])
    h_user = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    h_TODO = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)
    user = req.get(h_user).json()
    TODO = req.get(h_TODO).json()

    list_tasks = []
    for task in TODO:
        if task.get("completed") is True:
            list_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(list_tasks), len(TODO)))

    for task in list_tasks:
        print("\t {}".format(task))
