#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  /* let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count; */
  const nbOccurences = list.reduce((count, value) => {
    return value === searchElement ? count + 1 : count;
  }, 0);
  return nbOccurences;
};
