#!/usr/bin/python3
"""This script takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    payload = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        responsedict = r.json()
        if len(responsedict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(responsedict['id'], responsedict['name']))
    except Exception:
        print("Not a valid JSON")
