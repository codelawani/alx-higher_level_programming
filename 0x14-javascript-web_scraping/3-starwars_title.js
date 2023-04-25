#!/usr/bin/node
const movieApi = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const rq = require('request');
rq.get(
  { url: movieApi + movieId, encoding: 'utf-8' },
  (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).title);
    }
  }
);
