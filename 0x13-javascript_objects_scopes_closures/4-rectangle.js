#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (ch = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }

  rotate () {
    /* alternative solution 1
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
    alternative solution 2
    this.width = this.width ^ this.height;
    this.height = this.width ^ this.height;
    this.width = this.width ^ this.height; */
    // 1 liners :)
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
