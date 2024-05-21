#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  let charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  let dict = JSON.parse(body);
  for (let idx in dict.results) {
    if (dict.results[idx].characters.includes(charUrl)) {
      count++;
    }
  }
  console.log(count);
});
