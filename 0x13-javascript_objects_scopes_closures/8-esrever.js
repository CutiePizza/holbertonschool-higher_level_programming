#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    array.push(list[i]);
  }
  return array;
};
