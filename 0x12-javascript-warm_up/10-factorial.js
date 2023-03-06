#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
