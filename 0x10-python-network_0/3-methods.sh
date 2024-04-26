#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -s "$1" --request OPTIONS -I | grep Allow | sed 's/Allow: //'
