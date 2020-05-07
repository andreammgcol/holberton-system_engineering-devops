#!/usr/bin/python3
""" Function that queries the Reddit API """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        That returns a list containing the titles of all hot articles
        for a given subreddit. If no results are found for the given subreddit,
        the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    header = {'user-agent': 'X-Modash'}
    req = requests.get(url, headers=header)

    if req.status_code == 404:
        return None

    dict_json = req.json()
    hot_articles = dict_json.get('data').get('after')

    if hot_articles is not None:
        req = dict_json.get('data').get('children')
        for titles in req:
            titles = titles.get('data').get('titles')
            hot_list.append(titles)
        return recurse(subreddit, hot_list, hot_articles)
    else:
        return hot_list
