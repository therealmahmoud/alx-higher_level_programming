#!/usr/bin/node
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(process.argv[2], content, err => {
  if (err) {
    console.error(err);
  }
});
