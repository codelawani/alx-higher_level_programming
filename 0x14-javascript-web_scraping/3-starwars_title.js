#!/usr/bin/node
const api = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const rq = require('request');
rq.get({ url: api + id, encoding: 'utf-8' }, (err, response, body) => {
  if (!err) {
    console.log(JSON.parse(body).title);
  }
});
