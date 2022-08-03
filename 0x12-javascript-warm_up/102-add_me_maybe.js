#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (x, theFunction) {
  if (!isNaN(x)) {
    theFunction(parseInt(x) + 1);
  }
};
