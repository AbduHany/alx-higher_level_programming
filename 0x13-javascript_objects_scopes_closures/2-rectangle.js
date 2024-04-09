#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!(h <= 0 || w <= 0 || typeof w !== 'number' ||
    typeof h !== 'number')) {
      this.height = h;
      this.width = w;
    }
  }
};
