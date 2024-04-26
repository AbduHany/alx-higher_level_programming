#!/bin/bash
# causes the server to respond with a message containing You got me!
curl 0.0.0.0:5000/catch_me -s -X PUT -L -d "user_id=98" -H "Origin: School"
