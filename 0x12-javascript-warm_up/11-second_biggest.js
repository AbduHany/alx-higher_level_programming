#!/usr/bin/node
const len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  let sortedArr = process.argv.map((x) => Number(x));
  sortedArr = sortedArr.sort();
  console.log(sortedArr[1]);
}
