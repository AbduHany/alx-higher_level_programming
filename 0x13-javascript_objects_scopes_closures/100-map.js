#!/usr/bin/node
const list = require('./100-data.js').list;
let counter = 0;
const mappedList = list.map((x) => x * counter++);
console.log(list);
console.log(mappedList);
