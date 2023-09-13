#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

// Get movie ID from command line arguments
// as the first prositional argument
const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (response.statusCode === 200 && !error) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((characterUrl, index) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charResponse.statusCode === 200 && !charError) {
          const characterData = JSON.parse(charBody);
          console.log(`${characterData.name}`);
        } else {
          console.error(`Error fetching data from: ${charError}`);
        }
      });
    });
  }
}
);
