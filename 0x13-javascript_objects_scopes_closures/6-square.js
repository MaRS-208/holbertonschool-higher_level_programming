#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    const x = 'X';
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log(x.repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
