#!/usr/bin/node
const c = 'X';
const a = process.argv[2];
if (a && parseInt(a)) {
  for (let i = 0; i < a; i++) {
    console.log(c.repeat(a));
  }
}
else {
  console.log('Missing size');
}
