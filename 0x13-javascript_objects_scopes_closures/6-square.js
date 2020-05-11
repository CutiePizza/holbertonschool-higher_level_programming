#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i, j;
    for (i = 0; i < this.width; i++) {
      for (j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
