#!/usr/bin/node
// this script gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

if (process.argv.length === 4) {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
}
