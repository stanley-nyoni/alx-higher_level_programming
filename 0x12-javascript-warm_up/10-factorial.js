#!/usr/bin/node

let num = process.argv[2];
num = parseInt(num);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(num));
