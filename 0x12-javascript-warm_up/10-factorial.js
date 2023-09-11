#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (num) {
  if (num >= 1) return (num * factorial(num - 1));
  else return (1);
}

console.log(factorial(args[0]));
