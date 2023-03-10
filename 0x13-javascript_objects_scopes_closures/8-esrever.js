#!/usr/bin/node
exports.esrever = function (list) {
  /* let end = list.length - 1;
  const mid = list.length >> 1; // calculate midpoint using bitwise right shift
  // loop through first half of array
  for (let start = 0; start < mid; start++) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;
    end--;
  }
  return list; */
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
