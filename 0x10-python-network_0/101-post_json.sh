#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl "${1}" -s -X POST --header "Content-Type: application/json" -d "@${2}"
