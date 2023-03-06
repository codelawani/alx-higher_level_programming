#!/usr/bin/node
const num = process.argv.slice(2).sort().reverse()[1];
// second largest is the number at index 1 in the array
if (num) {
  console.log(num);
} else {
  console.log(0);
}
