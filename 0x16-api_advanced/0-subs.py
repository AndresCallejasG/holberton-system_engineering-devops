#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers
    for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    user_agent = {"User-Agent": "script:subs:v1 (by andrescallejasg)"}
    data = requests.get(url, headers=user_agent).json()
    try:
        subs = data['data']['subscribers']
    except KeyError:
        return(0)
    return (subs)
