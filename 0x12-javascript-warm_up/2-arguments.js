#!/usr/bin/node
let a = process.argv;
if(a.length === 2){
  console.log('No argument');
}
else if(a.length === 3){
  console.log('Argument found');
}
else{
  console.log('Arguments found');
}
