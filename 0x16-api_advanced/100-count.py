#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}.json?limit=100&after={after}"
    headers = {"User-Agent": "Mozilla/5.0", "raw_json": "1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for i in range(100):
                try:
                    hot_list.append(
                            data["data"]["children"][i]["data"]["title"]
                            )
                except Exception:
                    if len(hot_list):
                        pass
                    else:
                        return None
            if data["data"]["after"]:
                return recurse(subreddit, hot_list, data["data"]["after"])
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def count_words(subreddit, word_list):
    """
    queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """
    titles_list = recurse(subreddit, hot_list=[])
    if titles_list:
        word_count = {}
        for title in titles_list:
            title_words = title.split()
            for word in word_list:
                if word in title_words:
                    word_count[word] = word_count.get(word, 0) + 1
        word_count = dict(sorted(word_count.items(), key=lambda x: x[1]))
        word_count = dict(sorted(word_count.items(), key=lambda x: x[0]))
        for key, value in word_count.items():
            print(f"{key}: {value}")
