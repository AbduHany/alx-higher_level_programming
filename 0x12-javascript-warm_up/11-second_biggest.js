#!/usr/bin/node
const len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  let sortedArr = [];
  for (let i = 2; i < process.argv.length; i++) {
    sortedArr.push(Number(process.argv[i]));
  }
  sortedArr = sortedArr.sort();
  sortedArr = sortedArr.reverse();
  console.log(sortedArr[1]);
}
