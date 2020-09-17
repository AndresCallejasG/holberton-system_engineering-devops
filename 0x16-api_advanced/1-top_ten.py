#!/usr/bin/python3
""" queries the Reddit API and prints the titles
    of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """returns the hotests posts
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json?limit=10"
    user_agent = {"User-Agent": "script:subs:v1 (by andrescallejasg)"}
    data = requests.get(url, headers=user_agent).json()
    try:
        posts = data['data']['children']
    except KeyError:
        print("None")
        return
    for post in posts:
        print(post['data']['title'])
    return
