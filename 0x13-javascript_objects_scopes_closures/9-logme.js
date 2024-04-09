#!/usr/bin/node
let numberOfPrinted = 0;
exports.logMe = function (item) {
  console.log(numberOfPrinted++ + ': ' + item);
};
