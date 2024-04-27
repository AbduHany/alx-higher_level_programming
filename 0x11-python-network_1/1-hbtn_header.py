#!/usr/bin/python3
"""This python script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.info()['x-request-id'])
