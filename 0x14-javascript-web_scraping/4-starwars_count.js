#!/usr/bin/node
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// ID of the character "Wedge Antilles"
const characterId = 18;
const characterApi = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
// Make a request to the movies API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Filter the movies based on the presence of the character "Wedge Antilles"
  const wedgeMovies = movieData.results.reduce((count, movie) => {
    return movie.characters.includes(characterApi) ? count + 1 : count;
  }, 0);

  // Print the total number of movies where "Wedge Antilles" appears
  console.log(wedgeMovies);
});
