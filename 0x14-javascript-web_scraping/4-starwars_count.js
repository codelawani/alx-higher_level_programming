#!/usr/bin/node
const characterApi = 'https://swapi-api.alx-tools.com/api/people/';
const characterId = 18;
const rq = require('request');
rq.get(
  { url: characterApi + characterId, encoding: 'utf-8' },
  (err, response, body) => {
    if (!err) {
      //  Number of films specified character appears in
      console.log(JSON.parse(body).films.length);
    }
  }
);
