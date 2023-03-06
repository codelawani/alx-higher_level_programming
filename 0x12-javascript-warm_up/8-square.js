#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
/* ALTERNATE SOLUTION
  let i = arg;
  while (i-- > 0) {
    console.log('X'.repeat(arg));
  } */
}
