#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command-line argument

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(`HTTP status code: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    const charactersData = [];
    let charactersCount = 0;

    charactersUrls.forEach((characterUrl, index) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error: ${error}`);
        } else if (response.statusCode !== 200) {
          console.error(`HTTP status code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(body);
          charactersData[index] = characterData;
          charactersCount++;
          if (charactersCount === charactersUrls.length) {
            // All characters have been fetched, print their names
            charactersData.forEach((character) => {
              console.log(character.name);
            });
          }
        }
      });
    });
  }
});
