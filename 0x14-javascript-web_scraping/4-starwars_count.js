#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

if (process.argv.length === 3) {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const results = JSON.parse(body).results;
    let count = 0;
    for (const idx in results) {
      for (let i = 0; i < results[idx].characters.length; i++) {
        if (results[idx].characters[i].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  });
}
