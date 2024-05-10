#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys


def print_10(titles):
    """
    loops through the dict and prints it
    """
    for title in titles:
        print(title)


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0", "raw_json": "1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            titles = []
            for i in range(10):
                try:
                    titles.append(data["data"]["children"][i]["data"]["title"])
                except Exception:
                    if len(titles):
                        pass
                    else:
                        print(None)
                        sys.exit()
            print_10(titles)
            sys.exit()
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
