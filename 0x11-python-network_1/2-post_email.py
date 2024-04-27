#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
