#!/usr/bin/node
const s = 'C is fun';
const a = process.argv;
if (!a[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < a[2]; i++) { console.log(s); }
}
