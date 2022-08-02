#!/usr/bin/node
exports.esrever = function (list) {
  const rl = [];
  while (list.length) {
    rl.push(list.pop());
  }
  return (rl);
};
