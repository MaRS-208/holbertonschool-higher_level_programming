#!/usr/bin/node
const a = process.argv;
if (a[2]) {
  if (isNaN(parseInt(a[2]))) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(a[2]));
  }
} else {
  console.log('Not a number');
}
