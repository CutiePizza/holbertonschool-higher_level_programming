#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const string = body;
  fs.writeFile(filename, string, (error) => {
    if (error) throw error;
  });
});
