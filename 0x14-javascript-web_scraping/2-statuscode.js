#!/usr/bin/node
// This script displays the status code of a GET request.
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
