#!/usr/bin/node

exports.converter = function (base) {
  return function get (num) {
    return num.toString(base);
  };
};
