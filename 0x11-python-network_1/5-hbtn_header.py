#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the value of the variable `X-Request-Id` in the
response header
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1], timeout=0.1)
        print(r.headers['X-Request-Id'])
    except Exception as e:
        pass
