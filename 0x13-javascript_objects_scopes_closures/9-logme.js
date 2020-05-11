#!/usr/bin/node
var number = -1;
exports.logMe = function (item) {
  number++;
  console.log(number + ': ' + item);
};
