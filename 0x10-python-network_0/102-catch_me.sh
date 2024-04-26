#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl 0.0.0.0:5000/catch_me -s -X PUT -L -d "user_id=98"
