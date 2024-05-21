#!/usr/bin/node
// this script computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];

if (process.argv.length === 3) {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const result = JSON.parse(body);
    const total = {};
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        if (result[i].userId in total) {
          total[result[i].userId] = (total[result[i].userId] + 1);
        } else {
          total[result[i].userId] = 1;
        }
      }
    }
    console.log(total);
  });
}
