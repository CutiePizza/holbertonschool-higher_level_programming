#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(body.title);
});
