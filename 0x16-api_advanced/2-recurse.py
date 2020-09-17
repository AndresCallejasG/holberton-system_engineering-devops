#!/usr/bin/python3
""" queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns all the titles from the hottest posts
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    if after:
        url += "?after=" + after
    user_agent = {"User-Agent": "script:subs:v1 (by andrescallejasg)"}
    data = requests.get(url, headers=user_agent).json()
    try:
        posts = data['data']['children']
    except KeyError:
        print("None")
        return None

    for post in posts:
        hot_list.append(post['data']['title'])
    af = data['data']['after']
    if af:
        return recurse(subreddit, hot_list, af)
    return hot_list
