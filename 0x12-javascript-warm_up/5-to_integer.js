#!/usr/bin/node
const a = Number(process.argv[2]);
if (String(a) === 'NaN') {
  console.log('Not a number');
} else {
  console.log('My number: ' + a);
}
