#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let nb = number;
  theFunction(++nb);
};
