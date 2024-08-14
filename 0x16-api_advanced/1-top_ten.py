#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts listed
 for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = get(url, headers=user_agent, params=params)

        if response.status_code != 200:
            print("None")
            return

        results = response.json().get('data', {}).get('children', [])

        if not results:
            print("None")
            return

        for post in results:
            print(post.get('data', {}).get('title', "None"))

    except Exception:
        print("None")
