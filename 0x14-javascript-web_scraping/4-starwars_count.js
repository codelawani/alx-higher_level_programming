#!/usr/bin/node
const characterApi = 'https://swapi-api.alx-tools.com/api/people/18/';
const movieApi = process.argv[2];
const rq = require('request');
rq.get({ url: movieApi, encoding: 'utf-8' }, (err, response, body) => {
  if (!err) {
    //  Number of films specified character appears in
    let count = 0;
    for (const result of JSON.parse(body).results) {
      for (const c of result.characters) {
        if (c === characterApi) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
