#!/usr/bin/python3
""" Function that queries the Reddit API """

import requests


def number_of_subscribers(subreddit):
    """
        That returns the number of subscribers for a given subreddit.
        If an invalid subreddit is given, the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'X-Modash'}
    req = requests.get(url, headers=header)

    if req.status_code == 404:
        return 0

    dict_json = req.json()

    if 'data' in dict_json:
        return dict_json.get('data').get('subscribers')
    else:
        return 0
