#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/users/{}".format(usr)
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(pwd),
               'X-GitHub-Api-Version': '2022-11-28'}
    r = requests.get(url, headers=headers)
    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print("None")
