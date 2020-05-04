#!/usr/bin/python3
""" Python script to export data in the CSV format """

import csv
import json
import requests
import sys


if __name__ == "__main__":
    """ This export data in the CSV format """

    ID = int(sys.argv[1])
    urlUser = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    urlTODO = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)
    user = requests.get(urlUser).json()
    TODO = requests.get(urlTODO).json()

    with open('{}.csv'.format(ID), mode='w') as f:
        f_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in TODO:
            f_writer.writerow([ID, user.get('name'),
                               task.get('completed'), task.get('title')])
