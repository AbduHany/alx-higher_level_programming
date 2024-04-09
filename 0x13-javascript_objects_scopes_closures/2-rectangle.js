#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!(h <= 0 || w <= 0 || h === undefined || w === undefined)) {
      this.height = h;
      this.width = w;
    }
  }
};
