#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s "$1" -I | grep "Content-Length:" | sed 's/Content-Length: //'
