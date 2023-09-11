#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (!num1 || !num2) console.log('NaN');
else console.log(num1 + num2);
