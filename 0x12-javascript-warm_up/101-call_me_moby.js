#!/usr/bin/node
exports.callMeMoby = (x, theFunction) => {
  while (x-- > 0) {
    theFunction();
  }
};
