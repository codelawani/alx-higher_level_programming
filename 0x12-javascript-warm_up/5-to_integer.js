#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  const num = parseInt(argv[2]);
  console.log(num);
}
