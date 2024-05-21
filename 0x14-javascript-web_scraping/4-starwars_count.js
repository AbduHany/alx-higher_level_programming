#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  let count = 0;
  const dict = JSON.parse(body);
  for (const idx in dict.results) {
    if (dict.results[idx].characters.includes(charUrl)) {
      count++;
    }
  }
  console.log(count);
});
