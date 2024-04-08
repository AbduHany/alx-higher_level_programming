#!/usr/bin/node
const len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(1);
} else {
  const sortedArr = process.argv.sort();
  console.log(sortedArr[len - 2]);
}
