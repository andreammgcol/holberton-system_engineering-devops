#!/usr/bin/python3
""" Function that queries the Reddit API """

import requests


def top_ten(subreddit):
    """
        That returns the number of subscribers for a given subreddit.
        If an invalid subreddit is given, the function should return 0.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'user-agent': 'X-Modash'}
    req = requests.get(url, headers=header)

    if req.status_code == 404:
        print(None)
        return

    dict_json = req.json()

    if 'data' in dict_json:
        for hot_posts in dict_json.get('data').get('children'):
            print(hot_posts.get('data').get('title'))
    else:
        print(None)
