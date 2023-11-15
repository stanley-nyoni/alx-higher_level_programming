#!/usr/bin/node

let a = process.argv[2];
let b = process.argv[3];

a = parseInt(a);
b = parseInt(b);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
