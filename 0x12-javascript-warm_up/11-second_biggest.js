#!/usr/bin/node

const nums = process.argv.slice(2);

if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  nums.sort((a, b) => a - b);
  console.log(nums[nums.length - 2]);
}
