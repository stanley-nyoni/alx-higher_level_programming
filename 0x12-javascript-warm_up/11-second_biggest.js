#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(arg => parseInt(arg));
const validNums = nums.filter(num => !isNaN(num));
const sortedNums = validNums.sort((a, b) => b - a);

if (sortedNums.length === 0 || sortedNums.length === 1) {
  console.log(0);
} else {
  console.log(sortedNums[1]);
}
