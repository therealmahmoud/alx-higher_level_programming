#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  } else {
    const content = response.body;
    const fs = require('fs');
    fs.writeFile(process.argv[3], content, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
