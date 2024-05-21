#!/usr/bin/node
// prints all characters of a Star Wars Movie.
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

if (process.argv.length === 3) {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const charArr = JSON.parse(body).characters;
    for (let i = 0; i < charArr.length; i++) {
      request(charArr[i], (err, response, body) => {
        if (err) {
          console.error(err);
        }
        console.log(JSON.parse(body).name);
      });
    }
  });
}
