#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let i, j;
  const result = body.results;
  let n = 0;
  if (result !== undefined) {
    for (i = 0; i < result.length; i++) {
      const perso = result[i].characters;
      for (j = 0; j < perso.length; j++) {
        if (perso[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          n++;
          break;
        }
      }
    }
  }
  console.log(n);
});
