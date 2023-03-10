#!/usr/bin/node
exports.esrever = function (list) {
  let end = list.length - 1;
  const mid = parseInt(list.length / 2);
  for (let start = 0; start < mid; start++) {
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;
    end--;
  }
  return list;
};
