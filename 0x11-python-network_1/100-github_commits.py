#!/usr/bin/python3
"""This script lists the last 10 commits in a `repository` by
a `user`.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    ownr = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(ownr, repo)
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=headers)
    try:
        a = r.json()
        for i in range(10):
            print(a[i]['sha']+': '+a[i]['commit']['author']['name'])
    except Exception:
        pass
