#!/usr/bin/node

const fs = require('fs');

fs.writeFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  else {
    console.log(data)
  }
});
