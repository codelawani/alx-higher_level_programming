#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
/* exports.dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
}; */
const newDict = {};
for (const key in oldDict) {
  const value = oldDict[key];
  // check if the value in old dict is in the newDict
  /* if its there, push its key to the newDict
    example:
      oldDict
      key: value
      { 89: 1 }
      { 91: 1 }
      newDict
      key: value
      { 1: [89] } // on first iteration
      { 1: [89, 91]} // on second iteration
  */
  if (value in newDict) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
