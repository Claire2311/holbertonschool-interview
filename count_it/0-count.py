#!/usr/bin/python3
"""
Recursive count of keywords in Reddit hot article titles
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count occurrences of words in titles of hot articles in a subreddit."""
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + 1

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "HolbertonStudentAPI/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data")
    if not data:
        return

    children = data.get("children")
    if not children:
        return

    for post in children:
        title = post.get("data", {}).get("title", "")
        title_words = title.lower().split()

        for w in counts.keys():
            counts[w] += title_words.count(w)

    next_after = data.get("after")
    if next_after:
        return count_words(subreddit, word_list, next_after, counts)

    results = {k: v for k, v in counts.items() if v > 0}

    if not results:
        return

    sorted_results = sorted(results.items(),
                            key=lambda x: (-x[1], x[0]))

    for word, count in sorted_results:
        print(f"{word}: {count}")
