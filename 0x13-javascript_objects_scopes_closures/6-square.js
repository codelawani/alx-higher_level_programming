#!/usr/bin/node
const Square = require('./5-square');
class Square1 extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    /* This works due to the nature of my
    original print function */
    /*   print (ch = 'X') {
      for (let i = 0; i < this.height; i++) {
        console.log(ch.repeat(this.width));
      }
    } */
    super.print(c);
  }
}
module.exports = Square1;
